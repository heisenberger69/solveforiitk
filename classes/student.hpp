#pragma once
#include<string>
using namespace std;
class student
{
    public:
        string name;
        bool is_student;          //to check if a student is registered
        int roll_no;
        // int batch;
        // string mail_id; 
        // string branch;
        // long mobile_no;
        bool inside_status;       //if the student is inside the campus
        string visit_place;      
        // int room_no;
   
    public:

    void set_student(string Name,bool Inside_status)
    {
        name = Name;
        inside_status = Inside_status;
        is_student = true;
    }


};