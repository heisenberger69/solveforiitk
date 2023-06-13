from classes.employee import Employee
from classes.student import Student
from classes.visitor import Visitor
import pyttsx3

        

engine = pyttsx3.init()



import face_recognition
import cv2
import numpy as np
import io


known_image_paths = []

known_names = []  

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


students = [Student() for _ in range(1000)]
employees = [Employee() for _ in range(1000)]
visitors = [Visitor() for _ in range(1000)]

user_type = ""
user_index = 0







def new_student(name_of_student):
    students.append(name_of_student)

    known_image_paths.append('faces/' + name_of_student.name + '1.jpeg')
    known_image_paths.append('faces/' + name_of_student.name + '2.jpeg')

    known_names.append(name_of_student.name)
    known_names.append(name_of_student.name)
def new_employee(name_of_employee):
    employees.append(name_of_employee)

    known_image_paths.append('faces/' + name_of_employee.name + '1.jpeg')
    known_image_paths.append('faces/' + name_of_employee.name + '2.jpeg')

    known_names.append(name_of_employee.name)
    known_names.append(name_of_employee.name)
def new_visitor(name_of_visitor):
    visitors.append(name_of_visitor)

    known_image_paths.append('faces/' + name_of_visitor.name + '1.jpeg')
    known_image_paths.append('faces/' + name_of_visitor.name + '2.jpeg')

    known_names.append(name_of_visitor.name)
    known_names.append(name_of_visitor.name)    




    









def object_type(input):
    global user_type, user_index

    for i, student in enumerate(students):
        if student.name == input:
            user_type = "student"
            user_index = i
            break

    for i, visitor in enumerate(visitors):
        if visitor.name == input:
            user_type = "visitor"
            user_index = i
            break

    for i, employee in enumerate(employees):
        if employee.name == input:
            user_type = "employee"
            user_index = i
            break

    
            










dhruv = Student()
dhruv.set_student("dhruv",True)
new_student(dhruv)

hardick = Employee()
hardick.set_employee("hardick",False)
new_employee(hardick)

ayushmaan = Employee()
ayushmaan.set_employee("ayushmaan",False)
new_employee(ayushmaan)

anubhav = Visitor()
anubhav.set_visitor("anubhav",False)
new_visitor(anubhav)


rohit = Student()
rohit.set_student("rohit",True)
new_student(rohit)


nandini= Student()
nandini.set_student("nandini",True)
new_student(nandini)





def main():

     
    
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
        students[user_index].inside_status = False
        engine.say("Enjoy your visit to ")
        engine.say(str(destination))
        engine.runAndWait()


    elif user_type == "student" and students[user_index].name == input_name and students[user_index].inside_status == False:
        engine.say("student recognized successfully")
        engine.runAndWait()
        engine.say("welcome back to the campus")
        engine.runAndWait()
        
        students[user_index].visit_place = "campus"
        students[user_index].inside_status = True
       
    

    elif user_type == "employee" and  employees[user_index].name == input_name and employees[user_index].inside_status == True:
        engine.say("employee recognized successfully")
        engine.runAndWait()
        engine.say("happy journey")
        engine.runAndWait()
        employees[user_index].inside_status = False


    elif user_type == "employee" and  employees[user_index].name == input_name and employees[user_index].inside_status == False:
        engine.say("employee recognized successfully")
        engine.runAndWait()
        engine.say("welcome back to the campus")
        engine.runAndWait()
        employees[user_index].inside_status = True



    elif user_type == "visitor" and visitors[user_index].name == input_name and visitors[user_index].inside_status == True:
        engine.say("visitor recognized successfully")
        engine.runAndWait()
        engine.say("please come again")
        engine.runAndWait()
        visitors[user_index].inside_status == False

    elif user_type == "visitor" and visitors[user_index].name == input_name and visitors[user_index].inside_status == False:
        engine.say("visitor recognized successfully")
        engine.runAndWait()
        engine.say("You must leave the campus within 4 hours from now")
        engine.runAndWait()
        visitors[user_index].inside_status == True



    main()

if __name__ == "__main__":
    main()
