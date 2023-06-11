#pragma once
#include<string>
using namespace std;
class student
{
    private:
        string name;
        int roll_no;
        int batch;
        string mail_id;
        string branch;
        long mobile_no;
        bool inside_status;       //if the student is inside the campus
        string visit_place;      
        int room_no;
   
    public:

    void set_student(string Name,bool Inside_status)
    {
        name = Name;
        inside_status = Inside_status;
    }


};