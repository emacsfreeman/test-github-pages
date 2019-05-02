//
//  main.cpp
//  NestedStruct
//
//  Created by Laurent Garnier on 02/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

struct Employee
{
    short id;
    int age;
    double wage;
};

struct Company
{
    Employee CEO; // Employee is a struct within the Company struct
    int numberOfEmployees;
};

void printInformation(Employee employee)
{
    cout << "ID:    " << employee.id << "\n";
    cout << "AGE:   " << employee.age << "\n";
    cout << "WAGE:  " << employee.wage << "\n";
}

int main()
{
    Company myCompany = {{ 1, 42, 60000.0f }, 5 };
    cout << "CEO:\n";
    printInformation(myCompany.CEO);
    cout << endl;
    cout << "Company's members: " << myCompany.numberOfEmployees << endl;
    
    cout << "The size of Company is " << sizeof(Company) << "\n";
    cout << "The size of Employee is " << sizeof(Employee) << "\n";
    cout << "The size of CEO in Company is " << sizeof(myCompany.CEO) << "\n";
    cout << "The size of numberOfEmployees in Company is " << sizeof(myCompany.numberOfEmployees) << "\n";
    
    return 0;
}
