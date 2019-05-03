//
//  main.cpp
//  DateStruct
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

struct DateStruct
{
    int year;
    int month;
    int day;
};

void print(DateStruct &date)
{
    cout << date.year << "/" << date.month << "/" << date.day;
}

int main(int argc, const char * argv[])
{
    
    DateStruct today { 2020, 10, 14 }; // use uniform initialization
    
    today.day = 16; // use member selection operator to select a number of the struct
    print(today);
    
    return 0;
}
