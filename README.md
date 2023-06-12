Sure! Here's a sample README file for your project:

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


 add two or three images of each user in the faces folder with and name it name1.jpeg and name2.jpeg


 method 1  (without using sql):
   - in the line 34 of system.py ,  add path of each image in single quotes(examples given)
   - then in the line 37 of system.py, add names of the respective people in single quotes as many number of times 
     as the number of images of that person(examples given)
   - declare eveyone individually as student or employee just before the main fucntion

        example- dhruv = Employee()
                 hardick = Student()


   - now inside main
       set the attributes to employee objects like this-
       dhruv.set_employee("dhruv",False) 
             
       and student like this-
       hardick.set_student("hardick")


   - now add them to the students or employees list
       employees[0] = dhruv
       students[0] = hardick

 method 2 (using mysql)  (still have some bugs)
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

- Hardick Jindal
- Dhruv Mittal
- Nikhil Gupta
- Raghav Manglik



