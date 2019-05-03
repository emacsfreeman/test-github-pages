//
//  main.cpp
//  NestedStruct2
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

struct Marriage
{
    Person personA;
    Person personB;
    int ageOfMarriage;
    int numberOfPeopleAtWedding;
};

void printPersonInfo(Person p)
{
    cout << "The name of the person is " << p.name << endl;
    cout << "The age of the person is " << p.age << endl;
    cout << "The gender of the person is " << p.gender << endl;
}

void printMarriageInfo(Marriage m)
{
    cout << m.personA.name << " married " << m.personB.name << endl;
    cout << "They have been married for " << m.ageOfMarriage << " number of years." << endl;
    cout << m.numberOfPeopleAtWedding << " visited their wedding." << endl;
}

int main(int argc, const char * argv[])
{
    Person ivan = { "Ivan", 21, "male" };
    Person alex = { "Alex", 51, "male" };
    Person julia = { "Julia", 32, "female" };
    
    Marriage marriage = { alex, julia, 20, 200 };
    
    printMarriageInfo(marriage);
    
    return 0;
}
