//
//  main.cpp
//  ControlFlow
//
//  Created by Laurent Garnier on 29/04/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int number = 0;
    
    cout << "Please input a number: ";
    cin >> number;
    
    if (number < 10)
    {
        cout << "Your number is LESS than 10!" << endl;
    }
    else if (number >= 10 && number < 15)
    {
        cout << "Your number is greater or equal than 10 and below than 15" << endl;
    }
    else
    {
        cout << "Your number is greater or equal than 15" << endl;
    }
    
    
    return 0;
}
