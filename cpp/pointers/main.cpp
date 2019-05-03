//
//  main.cpp
//  Pointers
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

void increment(int* ptr)
{
    (*ptr)++;
}

int main()
{
    
    int myAge = 21;
    cout << "My age is: " << myAge << endl;
    cout << "The address of myAge is: " << &myAge << endl;
    
    int* ptr = &myAge;
    cout << "Pointer points to: " << ptr << endl;
    cout << "The pointer points to the value: " << (*ptr) << endl;

    cout << "\n===============================================\n\n";
    
    increment(ptr);
    cout << "Pointer STILL points to: " << ptr << endl;
    cout << "The pointer points to the INCREMENTED value: " << (*ptr) << endl;
    cout << "My age is NOW: " << myAge << endl;
    
    
    return 0;
}
