//
//  main.cpp
//  Constructors
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

class Person
{
public:
    string name;
    int age;
    string gender;
    
    Person(string n, int a, string g)
    {
        cout << "CONSTRUCTING OBJECT" << endl;
        name = n;
        age = a;
        gender = g;
    }
    
    Person()
    {
        cout << "Constructing without arguments" << endl;
        name = "Default name - No name provided";
        age = 99;
        gender = "female";
    }
    
    void printInfo()
    {
        cout << "The name of the person is " << name << endl;
        cout << "The age of the person is " << age << endl;
        cout << "The gender of the person is " << gender << endl;
    }
};

int main()
{
    Person ivan = Person();
    ivan.printInfo();
    
    Person laurent = Person("Laurent le boss", 36, "SIGMA MALE");
    laurent.printInfo();
    
    return 0;
}
