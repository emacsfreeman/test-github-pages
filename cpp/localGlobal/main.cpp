//
//  main.cpp
//  LocalGlobal
//
//  Created by Laurent Garnier on 29/04/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//


#include <iostream>

using namespace std;

int globalNumber = 10;

void printHello()
{
    // local variable
    string helloString = "hello\n";
    cout << helloString << "global number: " << globalNumber << endl;
}

void test()
{
    int a = 0;
    cout << "test " << a << " global number: " << globalNumber << endl;
}

int main(int argc, const char * argv[]) {
    
    printHello();
    test();
    
    // scope
    int b = 10;
    if (b < 20)
    {
        int hello = 30;
        cout << hello << endl;
    }
    
    //cout << hello << endl;
    
    return 0;
}
