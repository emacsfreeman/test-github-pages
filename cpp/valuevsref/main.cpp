//
//  main.cpp
//  ValueVSRef
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

void increaseByValue(int a)
{
    a++;
    cout << "Test number after increment in function 'increaseByValue': " << a << endl;
}

void increaseByRef(int& a)
{
    a++;
    cout << "Test number after increment in function 'increaseByRef': " << a << endl;
}

int main()
{
    
    // pass arguments by value and change them in the function,
    // the original DOESN'T change
    int testNumber = 5;
    increaseByValue(testNumber);
    
    cout << "Number after the function 'increaseByValue': " << testNumber << endl << endl;
    
    // pass arguments by reference and change them in the function,
    // the original DOES change
    int testNumber2 = 5;
    increaseByRef(testNumber2);
    
    cout << "Number after the function 'increaseByValue': " << testNumber2 << endl << endl;
    
    return 0;
}
