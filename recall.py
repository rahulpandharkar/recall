import cv2
import face_recognition
import numpy
 
# Load the image of Biden and learn how to recognize it
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
 
# Create a list of known face encodings and names
known_face_encodings = [biden_face_encoding]
known_face_names = ["Biden"]
 
# Initialize webcam
video_capture = cv2.VideoCapture(0)
 
while True:
    # Capture a single frame of video
    ret, frame = video_capture.read()
 
    # Resize frame for faster processing (optional)
    rgb_frame = numpy.ascontiguousarray(frame[:, :, ::-1])
 
    # Find all face locations in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
 
    # Process each detected face
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the detected face with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"  # Default name if no match is found
 
        # Check if a match was found
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        else:
            # Prompt for a new name if the face is unknown
            name = input("Enter name for the new face: ")
            known_face_encodings.append(face_encoding)
            known_face_names.append(name)
 
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
 
