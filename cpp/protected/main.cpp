//
//  main.cpp
//  Inheritance2
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

class Person
{
private:
    int age;
    string gender;
    int height;
    
protected:
    string name;
    
public:
    
    Person(string n, int a, string g)
    {
        cout << "CONSTRUCTING OBJECT!" << endl;
        name = n;
        age = a;
        gender = g;
        
        height = 1000;
    }
    
    void printInfo()
    {
        cout << "The name of the person is " << name << endl;
        cout << "The age of the person is " << age << endl;
        cout << "The gender of the person is " << gender << endl;
        cout << "The height of the person is " << height << endl;
    }
    
    void setHeight(int h)
    {
        if (h > 0)
            height = h;
        else
            height = 0;
    }
    
    // getter
    int getHeight()
    {
        return height;
    }
    
};

class Employee : public Person
{
public:
    int salary;
    Employee(string n, int a, string g) : Person(n, a, g)
    {
        salary = 100;
    }
    
    void printSalary()
    {
        cout << "The salary of " << name << " is " << salary << endl;
    }
    
};

int main()
{
    Employee ivan = Employee( "Ivan", 21, "male" );
    cout << "HEIGHT IS: " << ivan.getHeight();
    ivan.printInfo();
    ivan.printSalary();

    Person alex = Person("Alex", 23, "male");
    alex.printInfo();
    
    return 0;
}
