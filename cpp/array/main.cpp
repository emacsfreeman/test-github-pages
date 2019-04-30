//
//  main.cpp
//  Array
//
//  Created by Laurent Garnier on 30/04/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    cout << "5 first prime numbers\n";
    cout << "---------------------\n\n";
    
    int prime[5]; // hold the first 5 prime numbers
    prime[0] = 2; // The first element has index 0
    prime[1] = 3;
    prime[2] = 5;
    prime[3] = 7;
    prime[4] = 11; // The last element has index 4 (array length-1)
    
    for (int i = 0; i < 5; i++)
    {
        if (i == 4)
        {
            cout << prime[i] << "\n";
        }
        else
        {
            cout << prime[i] << ", ";
        }
        
    }
    
    cout << "\nThe lowest prime number is: " << prime[0] << "\n";
    cout << "The sum of the first 5 primes is: "
         << prime[0] + prime[1] + prime[2] + prime[3] + prime[4] << "\n";
    
    
    cout << "\nArray of doubles:\n";
    cout << "-----------------\n\n";
    
    double array[3]; // allocate 3 doubles
    array[0] = 2.0;
    array[1] = 3.0;
    array[2] = 4.3;
    
    cout << "The average is " << (array[0] + array[1] + array[2]) / 3 << "\n";
    
    
    cout << "\nUsing struct:\n";
    cout << "-------------\n";
    struct Rectangle
    {
        double length;
        double width;
    };
    Rectangle rects[5]; // declare an array of 5 Rectangle
    
    /*
    for (int i = 0; i < 5; i++)
    {
        cout << "Rectangle " << i << ": Please enter your data\n> length: ";
        cin >> rects[i].length;
        cout << "You typed, length = " << rects[i].length;
        cout << "\n> width: ";
        cin >> rects[i].width;
        cout << "You typed, width = " << rects[i].width << endl;
        cout << "It remains " << 4 - i << " rectangles to fill" << endl;
    }
     */
    
    cout << "\nOther arrays samples:\n";
    cout << "---------------------\n";
    
    int tab[5]; // declare an array of length 5
    
    // using a literal (constant) index:
    tab[1] = 7; // ok
    cout << "tab[1] = " << tab[1] << endl;
    
    // using an enum (constant) index
    enum Animals
    {
        ANIMAL_CAT = 2
    };
    tab[ANIMAL_CAT] = 4; // ok
    
    // using a variable (non-constant) index:
    short index = 3;
    tab[index] = 7; // ok
    
    // using an expression that evaluates to an integer index:
    tab[1+2] = 7; // ok
    
    // using a literal constant
    int tab2[5]; // Ok
    
    // using a macro symbolic constant
    #define ARRAY_LENGTH 5
    int tab3[ARRAY_LENGTH]; // Syntactically okay, but don't do this
    
    // using a symbolic constant
    const int arrayLength = 5;
    int tab4[arrayLength]; // Ok
    
    // using an enumerator
    enum ArrayElements
    {
        MAX_ARRAY_LENGTH = 5
    };
    int tab5[MAX_ARRAY_LENGTH]; // Ok

    
    return 0;
}
