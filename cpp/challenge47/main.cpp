//
//  main.cpp
//  Challenge47
//
//  Created by Laurent Garnier on 02/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    struct Employee
    {
        short id;
        int age;
        double wage;
    };
    
    Employee joe; // struct Employee is capitalized, variable joe is not.
    joe.id = 14; // assign a value to member id within struct joe
    joe.age = 32; // assign a value to member age within struct joe
    joe.wage = 24.15; // assign a value to member wage within struct joe
    
    Employee frank;
    frank.id = 15;
    frank.age = 28;
    frank.wage = 18.27;
    
    int totalAge = joe.age + frank.age;
    cout << totalAge << endl;
    
    if (joe.wage > frank.wage)
        cout << "Joe makes more than Frank\n";
    else if (joe.wage < frank.wage)
        cout << "Joe makes less than Frank\n";
    else
        cout << "Joe and Frank make the same amount\n";
    
    // Frank got a promotion
    frank.wage += 2.50;
    
    // Today is Joe's birthday
    ++joe.age; // use pre-increment to increment Joe's age by 1
    
    struct Employee2
    {
        short id;
        int age;
        double wage;
    };
    
    Employee joe2 = { 1, 32, 600000.0 }; // joe2.id = 1, joe2.age = 32, joe2.wage = 600000.0
    Employee frank2 = { 2, 28 }; // frank2.id = 2, frank2.wage = 0.0 (default initialization)
    
    Employee joe3 = { 1, 32, 600000.0 }; // joe3.id = 1, joe3.age = 32, joe3.wage = 600000.0
    Employee frank3 = { 2, 28 }; // frank3.id = 2, frank3.wage = 0.0 (default initialization)
    
   
    
    return 0;
}
