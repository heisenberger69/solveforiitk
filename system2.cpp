#include<bits/stdc++.h>
#include "classes/employee.hpp"
#include "classes/student.hpp"
#include "classes/visitor.hpp"

using namespace std;




vector<student> s(1000);                        //will be used to distinguish
vector<employee> e(1000);                       //the individual between the
vector<visitor> v(1000);                        //three classes until dataframe implementation is done



string user_type;                               //will be used to detect the type of 
string* ut = &user_type;                        //user who is on the gate while exiting

int user_index = 0;                             //index of the type of user
int* ui = &user_index;                          //who is on the gate while exiting


void object_type(string input)
{

   

    

    for(int i = 0; i < s.size(); i++)
    {
        if(s[i].name == input)
        {
            *ut = "student";
            *ui = i;
            break;
        }
    }


    for(int i =0; i < v.size(); i++)
    {
        if(v[i].name == input)
        {
            *ut = "visitor";
            *ui = i;
            break;
        }
    }

    for(int i = 0; i < e.size(); i++)
    {
        if(e[i].name == input)
        {
            *ut = "employee";
            *ui = i;
            break;
        }
    }
}






int main()
{
    student dhruv;
    

    visitor hardick;


    employee nikhil;


    dhruv.set_student("dhruv",true);
    hardick.set_visitor("hardick",false);
    nikhil.set_employee("nikhil",true);


 

    s[0] = dhruv;
    v[0] = hardick;
    e[0] = nikhil;

   




    //////////////EXITING/////////////

    cout<<"\nenter your name\n";                 //will be implemented by opencv
    string input;
    cin>>input;
     

    object_type(input);                                //changes the value of *ut to usertype and *ui to index of the usertype
    
   
    if(*ut == "student")                               //if the individual is of class student
    {
        cout<<"\nstudent recognised successfully\n";
        
        
        
        
        


         s[*ui].visit_place = "NA";
         s[*ui].inside_status = true;

         cout<<"welcome back "<<s[*ui].name;
         
         
    }



   
    else if(*ut == "employee")                       //if the individual is of class employee
    {
        cout<<"employee recognised successfully\n";

        e[*ui].inside_status = true;

        cout<<"welcome back "<<e[*ui].name<<"\n";
        
        
    }


    else                                              //definitely a visitor
    {
        
    }
   
    main();

}

