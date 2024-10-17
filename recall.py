import cv2
import face_recognition

# Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture a single frame of video
    ret, frame = video_capture.read()
    
    # Resize frame for faster processing (optional)
    rgb_frame = frame[:, :, ::-1]

    # Find all face locations in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Draw rectangles around detected faces and add "Hello"
    for (top, right, bottom, left) in face_locations:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Add the text "Hello" inside the rectangle
        cv2.putText(frame, "Hello", (left + 6, top + 30), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
video_capture.release()
cv2.destroyAllWindows()
