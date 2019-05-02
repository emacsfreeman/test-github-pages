//
//  main.cpp
//  ForStatements
//
//  Created by Laurent Garnier on 02/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

int pow(int base, int exponent)
{
    int total = 1;
    
    for (int count = 0; count < exponent; ++count)
        total *= base;
    
    return total;
}

// Assignement 2
int sumTo(int number)
{
    int sum = 0;
    for (int count = 0; count <= number; ++count)
    {
        sum += count;
    }
    return sum;
}

int main()
{
    for (int count = 0; count < 10; ++count)
    {
        cout << count << " ";
    }
    
    cout << endl;
    
    int count = 0;
    while (count < 10)
    {
        cout << count << " ";
        ++count;
    }
    
    cout << endl;
    
    cout << "2^6 = " << pow(2, 6) << endl;
    
    for (int count = 9; count >= 0; --count)
    {
        cout << count << " ";
    }
    
    cout << endl;
    
    for (int count = 9; count >= 0; count -= 2)
    {
        cout << count << " ";
    }
    
    cout << endl;
    
    int count2 = 0;
    for (; count2 < 10; )
    {
        cout << count2 << " ";
        ++count2;
    }
    
    int iii, jjj;
    for (iii=0, jjj=9; iii < 10; ++iii, --jjj)
    {
        cout << iii << " " << jjj << '\n';
    }
    
    for (int iii=0, jjj=9; iii < 0; ++iii, --jjj)
    {
        cout << iii << " " << jjj << '\n';
    }
    
    for (int count=0; count < 10; ++count)
    {
        cout << count << " ";
    }
    
    cout << '\n';
    cout << "I counted to: " << count << "\n";
    
    for (char c = 'a'; c <= 'e'; ++c)
    {
        cout << c;
        
        for (int i = 0; i < 3; ++i)
        {
            cout << i;
        }
        
        cout << '\n';
    }
    
    
    // Assignement 1
    for (int number = 0; number <= 20; ++number)
    {
        if (number % 2 == 0)
            cout << "number = " << number << endl;
    }
    
    // Assignement 2
    cout << sumTo(10) << endl;
    
    
    return 0;
    
}
