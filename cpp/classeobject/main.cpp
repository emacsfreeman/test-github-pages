//
//  main.cpp
//  ClassesObjects
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
    
    void printInfo()
    {
        cout << "The name of the person is " << name << endl;
        cout << "The age of the person is " << age << endl;
        cout << "The gender of the person is " << gender << endl;
    }
};

int main()
{
    Person ivan = {"Ivan", 21, "male"};
    ivan.printInfo();
    
    return 0;
}

