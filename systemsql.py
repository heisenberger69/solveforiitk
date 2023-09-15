
from classes.student import Student
import pyttsx3

import mysql.connector

        
connection = mysql.connector.connect(host='localhost',
                                     database='DATA',
                                     user='root',
                                     password = 'Raghav')


cursor = connection.cursor()
query = ("SELECT * FROM STUDENTS ;")
cursor.execute(query)
rows = cursor.fetchall()
students = []
known_image_paths = []
known_names = []

for row in rows:
    obj = Student()
    obj.set_student(row[0],row[2])     
    pat = [row[4], row[5] , row[6]]
    name = [row[0],row[0],row[0]]
    students.append(obj)
    known_image_paths.append(pat)
    known_names.append(name)

connection.close()
       

engine = pyttsx3.init()



import face_recognition
import cv2
import numpy as np
import io



def facedetect():

    cap = cv2.VideoCapture(0)
    _,feed = cap.read()

    cv2.imshow("frame",feed)

    cv2.waitKey(3000)
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        exit()

    frame_jpg = cv2.imencode('.jpg', frame)[1].tobytes()

    cap.release()
    cv2.destroyAllWindows()

    known_face_encodings = []


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

        return name








import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()
def textfromspeech():

    with m as source: r.adjust_for_ambient_noise(source)

    print("Say something!")
    with m as source: audio = r.listen(source,timeout = 5)

    value = r.recognize_google(audio)
    return value


user_type = ""
user_index = 0













def object_type(input):
    global user_type, user_index

    for i, student in enumerate(students):
        if student.name == input:
            user_type = "student"
            user_index = i
            break

    


def main():
    
    connection = mysql.connector.connect(host='localhost',
                                        database='DATA',
                                        user='root',
                                        password = 'Raghav')


    cursor = connection.cursor()
     
    
    input_name = facedetect()  
    # input_name = input()       

    object_type(input_name)
    print(input_name)

    if user_type == "student" and students[user_index].name == input_name and students[user_index].inside_status == True:
        engine.say("student recognized successfully")
        engine.runAndWait()
        engine.say("where do you wish to go")
        engine.runAndWait()
        destination = textfromspeech()
        
        
        students[user_index].visit_place = destination
        query = ("UPDATE STUDENTS SET visiting = %s where name = %s")
        cursor.execute(query,(destination,input_name,))        
        students[user_index].inside_status = False
        query = ("UPDATE STUDENTS SET in_status = 0 where name = %s ;")
        cursor.execute(query(input_name,))           
        engine.say("Enjoy your visit to ")
        engine.say(str(destination))
        engine.runAndWait()


    elif user_type == "student" and students[user_index].name == input_name and students[user_index].inside_status == False:
        engine.say("student recognized successfully")
        engine.runAndWait()
        engine.say("welcome back to the campus")
        engine.runAndWait()
        query = ("UPDATE STUDENTS SET visiting = %s Where name = %s ;")
        cursor.execute(query,("campus",input_name,))        
        students[user_index].inside_status = False
        query = ("UPDATE STUDENTS SET in_status = 1 Where name = %s ;")
        cursor.execute(query,(input_name,))
        students[user_index].visit_place = "campus"
        students[user_index].inside_status = True
    
    connection.close()
    

    main()

if __name__ == "_main_":
    main()