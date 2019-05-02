//
//  main.cpp
//  Employee
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

void printInformation(Employee employee)
{
    cout << "ID:   " << employee.id << "\n";
    cout << "Age:  " << employee.age << "\n";
    cout << "Wage: " << employee.wage << "\n";
}

int main()
{
    Employee joe = { 14, 32, 24.15 };
    Employee frank = { 15, 28, 18.27 };
    
    // Print Joe's information
    printInformation(joe);
    
    cout << "\n";
    
    // Print Frank's information
    printInformation(frank);
    
    return 0;
    
}


