from classes.employee import Employee
from classes.student import Student
from classes.visitor import Visitor
import pyttsx3
engine = pyttsx3.init()


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

def main():
    dhruv = Student()
    ayushmaan = Student()
    hardick = Visitor()
    nikhil = Employee()
    
    
    dhruv.set_student("dhruv", True)
    ayushmaan.set_student("ayushmaan",True)
    hardick.set_visitor("hardick", False)
    nikhil.set_employee("nikhil", True)

    students[0] = dhruv
    students[1] = ayushmaan
    visitors[0] = hardick
    employees[0] = nikhil

    print("Enter your name:")
    input_name = input()                 #through face recognition

    object_type(input_name)

    if user_type == "student":
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
    

    elif user_type == "employee":
        engine.say("employee recognized successfully")
        engine.runAndWait()
        employees[user_index].inside_status = False

    elif user_type == "visitor":
        engine.say("visitor recognized successfully")
        engine.runAndWait()

    main()

if __name__ == "__main__":
    main()
