//
//  main.cpp
//  Struct
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

struct Person
{
    string name;
    int age;
    string gender;
};

void printPersonInfo(Person p)
{
    cout << "The name of the person is " << p.name << endl;
    cout << "The age of the person is " << p.age << endl;
    cout << "The gender of the person is " << p.gender << endl;
}

int main(int argc, const char * argv[])
{
    
    Person ivan;
    ivan.name = "Ivan";
    ivan.gender = "male";
    ivan.age = 21;
    
    Person josh;
    josh.name = "Josh";
    josh.gender = "male";
    josh.age = 26;
    
    Person people[] = { ivan, josh };
    
    printPersonInfo(people[0]);

    
    return 0;
}
