//
//  main.cpp
//  Classes
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

class DateClass
{
public:
    int m_year;
    int m_month;
    int m_day;
    
    void print() // defines a member function named print()
    {
        cout << m_year << "/" << m_month << "/" << m_day << endl;
    }
};


int main()
{
    
    DateClass today { 2020, 10, 14 };
    
    today.m_day = 16; //use member selction operator to select a member variable of the class
    today.print(); // use member selection operator to call a member function of the class
    
    return 0;
}
