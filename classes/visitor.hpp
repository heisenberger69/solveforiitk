#include<string>
#include</home/dhruvmittal/Desktop/genai/classes/student.hpp>
using namespace std;



class visitor
{
    public:
        string name;
        bool is_visitor;
        long mobile_no;
        student* student_ptr;
        int visitor_id;
        int vehicle_no;
        int govt_id;
        bool inside_status;


    public:

    void set_visitor(string Name,bool Inside_status)
    {
        name = Name;
        inside_status = Inside_status;
        is_visitor = true;
    }
        
};