from classes.employee import Employee
from classes.student import Student
from classes.visitor import Visitor

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
    hardick = Visitor()
    nikhil = Employee()

    dhruv.set_student("dhruv", True)
    hardick.set_visitor("hardick", False)
    nikhil.set_employee("nikhil", True)

    students[0] = dhruv
    visitors[0] = hardick
    employees[0] = nikhil

    print("Enter your name:")
    input_name = input()

    object_type(input_name)

    if user_type == "student":
        print("Student recognized successfully.")
        print("Enter visit place:")
        destination = input()
        students[user_index].visit_place = destination
        students[user_index].inside_status = False
        print("Enjoy your visit to", destination)

    elif user_type == "employee":
        print("Employee recognized successfully.")
        employees[user_index].inside_status = False

    elif user_type == "visitor":
        print("Visitor recognized successfully.")

    main()

if __name__ == "__main__":
    main()
