//
//  main.cpp
//  Array2
//
//  Created by Laurent Garnier on 30/04/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>
#include <iterator> // for std::size

using namespace std;

void passValue(int value) // value is a copy of the argument
{
    value = 99; // so changing it here won't change the value of the argument
}

void passArray(int prime[5]) // prime is the actual array
{
    prime[0] = 11; // so changing it here will change the original argument!
    prime[1] = 7;
    prime[2] = 5;
    prime[3] = 3;
    prime[4] = 2;
}

void printSize(int array[])
{
    cout << sizeof(array) << '\n'; // prints the size of a pointer, not the size of the array!
}


int main(int argc, const char * argv[]) {
    
    int value = 1;
    cout << "before passValue: " << value << "\n";
    passValue(value);
    cout << "after passValue: " << value << "\n";
    
    int prime[5] = { 2, 3, 5, 7, 11 };
    cout << "before passArray: " << prime[0] << " " << prime[1] << " " << prime[2] << " " << prime[3] << " " << prime[4] << "\n";
    passArray(prime);
    cout << "after passArray: " << prime[0] << " " << prime[1] << " " << prime[2] << " " << prime[3] << " " << prime[4] << "\n";
    
    int array[5] = { 7, 4, 5 }; // only initialize first 3 elements
    
    cout << array[0] << '\n';
    cout << array[1] << '\n';
    cout << array[2] << '\n';
    cout << array[3] << '\n';
    cout << array[4] << '\n';
    
    // Initialize all elements to 0.0
    double darray[5] = { };
    
    
    enum StudentNames
    {
        KENNY, // 0
        KYLE, // 1
        STAN, // 2
        BUTTERS, // 3
        CARTMAN, // 4
        MAX_STUDENTS // 5
    };
    
    int testScores[MAX_STUDENTS]; // allocate 5 integers
    testScores[STAN] = 76;
    
    
    int array2[] = { 1, 1, 2, 3, 5, 8, 13, 21 };
    cout << sizeof(array2) << '\n'; // will print the size of the array
    printSize(array2);
    
    int array3[] = { 1, 1, 2, 3, 5, 8, 13, 21 };
    cout << "The array has: " << sizeof(array3) / sizeof(array3[0]) << " elements\n";
    
   
    
    return 0;
}
