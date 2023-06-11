#include<string>
using namespace std;

class employee
{
    private:
        string name;
        int mobile_no;
        bool inside_status;


    public:  

    void set_employee(string Name,bool Inside_status)
    {
        name = Name;            
        inside_status = Inside_status;
    }




};