import face_recognition
import cv2
import numpy as np
import io

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Wait for a few seconds to allow the camera to warm up
cv2.waitKey(3000)

# Read a frame from the webcam
ret, frame = cap.read()

# If the frame is not captured successfully, exit the program
if not ret:
    print("Failed to capture frame")
    exit()

# Convert the frame to JPEG format in memory
frame_jpg = cv2.imencode('.jpg', frame)[1].tobytes()

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()

# Load and encode known faces
known_image_paths = ['faces/nikhil.jpeg', 'faces/ayushmaan.jpeg', 'faces/dhruv.jpeg', 'faces/anubhav.jpeg', 'faces/hardick.jpeg','faces/agam.jpeg']
known_face_encodings = []

for image_path in known_image_paths:
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)

# Load the unknown image
unknown_image = face_recognition.load_image_file(io.BytesIO(frame_jpg))

# Find face locations and encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Compare face encodings of unknown faces with known faces
for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    if True in matches:
        first_match_index = matches.index(True)
        name = f"Known Face {first_match_index + 1}"

    print(f"Face recognized: {name}")
