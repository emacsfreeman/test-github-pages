//
//  main.cpp
//  Template
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

template <class T>
T multiply(T a, T b)
{
    return a * b;
}

int main()
{
    cout << multiply(5.5, 4.4) << endl;
    return 0;
}
