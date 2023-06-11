import face_recognition

# Load and encode known faces
known_image_paths = ['faces/nikhil.jpeg','faces/ayushmaan.jpeg','faces/dhruv.jpeg','faces/anubhav.jpeg','faces/hardick.jpeg']
known_face_encodings = []

for image_path in known_image_paths:
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)

# Load an unknown image
unknown_image_path = 'faces/anubhavtest.jpeg'
unknown_image = face_recognition.load_image_file(unknown_image_path)

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
