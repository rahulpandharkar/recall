import cv2
import face_recognition
import numpy as np
import threading
import time
import pyttsx3
import speech_recognition as sr

# Load the image of Biden and learn how to recognize it
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create a list of known face encodings and names
known_face_encodings = [biden_face_encoding]
known_face_names = ["Biden"]

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Initialize the text-to-speech engine with Indian English voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if 'India' in voice.name:
        engine.setProperty('voice', voice.id)
        break
# Set voice properties for clarity and natural flow
engine.setProperty('rate', 150)  # Adjust speaking rate if needed
engine.setProperty('volume', 1.0)  # Full volume

# Recognizer for speech input
recognizer = sr.Recognizer()

# Global variables
new_face_name = None
last_announced = ""
input_lock = threading.Lock()

# Function to get audio input for a new name
def get_audio_name():
    global new_face_name
    while True:
        with sr.Microphone() as source:
            print("Listening for name...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5)  # wait up to 5 seconds for input
                name = recognizer.recognize_google(audio, language="en-IN")
                with input_lock:
                    new_face_name = name
                    print(f"Received new face name: {name}")
            except sr.UnknownValueError:
                print("Could not understand the name.")
            except sr.RequestError:
                print("Could not request results; check your network connection.")
            except sr.WaitTimeoutError:
                print("Listening timed out waiting for input.")
        
        # Delay to prevent the mic from being accessed too frequently
        time.sleep(3)

# Function to announce names when updated
def announce_names():
    global last_announced
    while True:
        if last_announced:
            # Use a friendly message format for announcements
            if last_announced == "Unknown Person":
                engine.say("Unknown person detected")
            else:
                engine.say(f"Hello, {last_announced}")
            engine.runAndWait()
            time.sleep(5)  # Delay between announcements

# Start threads for audio input and name announcements
audio_thread = threading.Thread(target=get_audio_name, daemon=True)
audio_thread.start()

announce_thread = threading.Thread(target=announce_names, daemon=True)
announce_thread.start()

while True:
    # Capture a single frame of video
    ret, frame = video_capture.read()
    if not ret:
        break  # If frame capture fails, exit the loop

    # Resize frame for faster processing (optional)
    rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Process each detected face
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the detected face with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown Person"  # Default name if no match is found

        # Check if a match was found
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        else:
            # If face is unknown and a name is being provided, add it to the list
            with input_lock:
                if new_face_name is not None:
                    known_face_encodings.append(face_encoding)
                    known_face_names.append(new_face_name)
                    name = new_face_name  # Use the new name for immediate display
                    new_face_name = None  # Reset after adding

        # Update announcement name if different from the last one announced
        if last_announced != name:
            last_announced = name

        # Draw a rectangle around the face and add the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left + 6, top + 30), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
video_capture.release()
cv2.destroyAllWindows()
