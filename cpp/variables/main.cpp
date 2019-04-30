//
//  main.cpp
//  Variables
//
//  Created by Laurent Garnier on 29/04/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    // variables have types
    
    // first type int (integer) ONLY WHOLE NUMBERS
    cout << "DATA TYPE: int for INTEGER which means WHOLE numbers" << endl;
    cout << "----------------------------------------------------" << endl;
    
    int a = 3;
    char aStr[] = "a = ";
    int b = 5;
    int c = a * b - a;
    
    cout << aStr;
    cout << a << endl;
    cout << "b = " << b << endl;
    cout << "c = " << c << endl;
    cout << "====================================================" << endl;
    
    // second type boolean (true/false)
    cout << "\nDATA TYPE: bool for BOOLEAN which means true or false" << endl;
    cout << "------------------------------------------------------" << endl;
    
    bool d = true; // = 1
    bool e = false; // = 0
    bool k = d || e;
    cout << "d = " << d << endl;
    cout << "e = " << e << endl;
    cout << "k = " << k << endl;
    
    // third type double and float
    cout << "\nDATA TYPE: float for FLOATING point numbers or double for  double precision numbers" << endl;
    cout << "------------------------------------------------------------------------------------" << endl;
    
    double h = 0.9;
    double j = 0.3;
    double result = h + j;
    
    cout << "h = " << h << endl;
    cout << "j = " << j << endl;
    cout << "result = " << result << endl;
    cout << "===================================================================================" << endl;
    
    return 0;
}
