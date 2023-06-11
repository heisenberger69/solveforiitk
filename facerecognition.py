import face_recognition
import cv2
import numpy as np
import io

def facedetect():

    cap = cv2.VideoCapture(0)
    cv2.waitKey(3000)
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        exit()

    frame_jpg = cv2.imencode('.jpg', frame)[1].tobytes()

    cap.release()
    cv2.destroyAllWindows()

    known_image_paths = [ 'faces/dhruv.jpeg', 'faces/anubhav.jpeg', 'faces/hardick.jpeg','faces/hardick2.jpeg','faces/hardick3.jpeg','faces/hardick3.jpeg', 'faces/agam.jpeg']
    known_face_encodings = []

    known_names = ['dhruv','anubhav','hardick','hardick','hardick','hardick','agam']  

    for image_path in known_image_paths:
        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)


        
        name = image_path.split('/')[-1].split('.')[0]  
        known_names.append(name)

    unknown_image = face_recognition.load_image_file(io.BytesIO(frame_jpg))

    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]  

        # print(f"Face recognized: {name}")
        return name


print(facedetect())