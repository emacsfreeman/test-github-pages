//
//  main.cpp
//  Quizz47Part2
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

/*
 My solution
#include <iostream>

using namespace std;

struct Fraction
{
    int numerator;
    int denominator;
};

double multiply(Fraction frac1, Fraction frac2)
{
    return frac1.numerator * frac2.numerator / frac1.denominator * frac2.denominator;
}

int main()
{
    Fraction frac1;
    cout << "Fraction1" << endl;
    cout << "numerator: ";
    cin >> frac1.numerator;
    cout << "denominator: ";
    cin >> frac1.denominator;
    

    Fraction frac2;
    cout << "Fraction2" << endl;
    cout << "numerator: ";
    cin >> frac2.numerator;
    cout << "denominator: ";
    cin >> frac2.denominator;
    
    cout << multiply(frac1, frac2) << endl;
    
    
    return 0;
}
 */

// Their solution

#include <iostream>

struct Fraction
{
    int numerator;
    int denominator;
};

Fraction getFraction()
{
    Fraction temp;
    std::cout << "Enter a value for numerator: ";
    std::cin >> temp.numerator;
    std::cout << "Enter a value for denominator: ";
    std::cin >> temp.denominator;
    std::cout << "\n";
    return temp;
}

void multiply(Fraction f1, Fraction f2)
{
    // Don't forget the static cast, otherwise the compiler will do integer division!
    std::cout << static_cast<float>(f1.numerator * f2.numerator) /
    (f1.denominator* f2.denominator);
}

int main()
{
    // Allocate our first fraction
    Fraction f1 = getFraction();
    Fraction f2 = getFraction();
    
    multiply(f1, f2);
    
    return 0;
}
