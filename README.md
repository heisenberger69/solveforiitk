# Face Recognition System

This project is a face recognition system that identifies individuals and manages their access to a facility or campus. The system recognizes registered students, employees, and visitors(to be implemented) based on their faces and performs appropriate actions based on their recognition status.

## Features

- Face detection and recognition using the face_recognition library
- Voice prompts and responses using the pyttsx3 library
- Speech recognition for user input using the SpeechRecognition library
- Object-oriented programming approach with classes for Student, Employee, and Visitor
- Integration of face recognition, speech recognition, and object management

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/heisenberger69/genai.git
   ```

2. Install the required dependencies. Make sure you have Python 3 and pip installed, and then run:

   ```bash
   pip install -r requirements.txt
   ```

3. To register faces:


 add two (or three for sql) images of each user in the faces folder with and name it name1.jpeg and name2.jpeg


 method 1  (without using sql):
   ```
   -type 


    name = Student()
    name.set_student("name",True(or False if you want the student to be outside the campus initially))
    new_student(name)
    ```
    or 
    ```
    name = Employee()
    name.set_employee("name",True(or False if you want the employee to be outside the campus initially ))
    new_employee(name)
    ```
    or 
    
    ```
    name = Visitor()
    name.set_visitor("name",True(or False if you want the visitor to be outside the campus initially ))
    new_visitor(name)


    just before the main to register students,employees and visitors
    ```

 method 2 (using mysql)  (still have some bugs and only for students)
   - first install mysql server and start a server
   - then in the terminal that is running mysql, run


    

            
        Create Data ;
    Use Data ;
    Create table Students ( name varchar(50) , roll int , status_in int , visiting_place varchar(50) , path1 varchar(100) , path2 varchar(100) , path3 varchar(100);
    Insert into Students values( “name” , 0001 , 0 , “Delhi” ,  “faces/name1.jpeg” , “faces/name2.jepg” , “faces/name3.jpeg”);
    


     







3. Run the main script to start the face recognition system:

   ```bash
   python3 system.py

   or 

   python3 systemsql.py
   ```





## Contributors

- Hardik Jindal
- Dhruv Mittal
- Nikhil Gupta
- Raghav Manglik



