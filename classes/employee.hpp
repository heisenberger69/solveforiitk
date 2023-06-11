#include<string>
using namespace std;

class employee
{
    public:
        string name;
        int employee_no;
        bool is_employee;
        // int mobile_no;
        bool inside_status;


    public:  

    void set_employee(string Name,bool Inside_status)
    {
        name = Name;            
        inside_status = Inside_status;
        is_employee = true;
    }




};