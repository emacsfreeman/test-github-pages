//
//  main.cpp
//  Functions
//
//  Created by Laurent Garnier on 29/04/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

void test()
{
    cout << "This is a void function." << endl;
    cout << "Which means that it doesn't return any value." << endl;
}

int multiply(int x, int y)
{
    return x * y;
}

string createGreeting(string name)
{
    return "Greetings " + name + "\n";
}

int main(int argc, const char * argv[]) {
    // test void function
    cout << "Void function:\n";
    cout << "--------------\n\n";
    cout << "test() = \n";
    test();
    
    // test int function
    cout << "\nFunction that returns int\n";
    cout << "-------------------------\n\n";
    int answer = multiply(2, 3);
    cout << "multiply(2, 3) = " << "2 x 3 = " << answer << endl;
    
    // test string function
    cout << "\nFunction that returns string\n";
    cout << "----------------------------\n\n";
    cout << "What's your name? ";
    string name;
    cin >> name;
    cout << "createGreeting(name) = " << createGreeting(name) << endl;
    
    return 0;
}
