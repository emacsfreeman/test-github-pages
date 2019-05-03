//
//  main.cpp
//  InPair
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//


/*
// My solution
#include <iostream>

using namespace std;

class IntPair
{
public:
    int m_num1;
    int m_num2;
    
    void set(int num1, int num2)
    {
        m_num1 = num1;
        m_num2 = num2;
    }
    
    void print()
    {
        cout << "m_num1 = " << m_num1 << endl;
        cout << "m_num2 = " << m_num2 << endl;
        
    }
};


int main()
{
    IntPair p1;
    p1.set(1, 1); // set p1 values to (1, 1)
    
    IntPair p2{ 2, 2 }; // initialize p2 values to (2, 2)
    
    cout << "p1: " << endl;
    cout << "---" << endl;
    p1.print();
    cout << "==============" << endl;
    
    cout << "p2: " << endl;
    cout << "---" << endl;
    p2.print();
    
    
    return 0;
}
 
 */

// Their solution
#include <iostream>

class IntPair
{
public:
    int m_first;
    int m_second;
    
    void set(int first, int second)
    {
        m_first = first;
        m_second = second;
    }
    void print()
    {
        std::cout << "Pair(" << m_first << ", " << m_second << ")\n";
    }
};

int main()
{
    IntPair p1;
    p1.set(1, 1);
    
    IntPair p2{ 2, 2 };
    
    p1.print();
    p2.print();
    
    return 0;
}
