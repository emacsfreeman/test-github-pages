//
//  main.cpp
//  TypeDef
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

typedef double height;

struct HomoSapiens
{
    string name;
};

typedef HomoSapiens Person;

int main()
{
    height ivanHeight = 191.5;
    Person person;
    person.name = "Ivan";
    
    cout << person.name << " height: " << ivanHeight << endl;
    
    return 0;
}
