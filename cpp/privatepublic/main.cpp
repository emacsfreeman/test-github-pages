//
//  main.cpp
//  PublicPrivate
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;


class Person
{
private:
    int height;
    string name;
    int age;
    string gender;
    
public:
    
    
    Person(string n, int a, string g)
    {
        cout << "CONSTRUCTING OBJECT!" << endl;
        name = n;
        age = a;
        gender = g;
        
        height = 1000;
    }
    
    void printInfo()
    {
        cout << "The name of the person is " << name << endl;
        cout << "The age of the person is " << age << endl;
        cout << "The gender of the person is " << gender << endl;
        cout << "The height of the person is " << height << endl;
    }
    
    void setHeight(int h)
    {
        if (h > 0)
            height = h;
        else
            height = 0;
    }
    
    // getter
    int getHeight()
    {
        return height;
    }
    
};

int main()
{
    
    Person ivan = Person("Ivan", 21, "male");
    ivan.setHeight(-555);
    cout << "Try to set a negative height:" << endl;
    cout << "==============================" << endl;
    ivan.printInfo();
    cout << "==============================" << endl;
    ivan.setHeight(555);
    cout << "With a positive height:" << endl;
    ivan.printInfo();
    cout << "==============================" << endl;
    ivan.setHeight(300);
    cout << "HEIGHT IS: " << ivan.getHeight() << endl;
    
    // cout << "Reading height: " << ivan.height << endl; // WRONG PRACTICE, DOESN'T WORK
    
    return 0;
}
