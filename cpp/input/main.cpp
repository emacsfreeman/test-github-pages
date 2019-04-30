//
//  main.cpp
//  Input
//
//  Created by Laurent Garnier on 29/04/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//


#include <iostream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    /*
        1) Get the name of the user
        2) Print "Good Morning " + User Name
     */
    string name = "";
    cout << "What's your name?" << endl;
    
    getline(cin, name);
    cout << "Good Morning " << name << endl;
    
    int age = 0;
    cout << "How old are you?" << endl;
    cin >> age;
    cout << "Oh you are " << age << " years old" << endl;
    
    return 0;
}
