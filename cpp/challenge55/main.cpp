//
//  main.cpp
//  Challenge55
//
//  Created by Laurent Garnier on 02/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    char myChar = 'a';
    while (myChar <= 'z')
    {
        cout << myChar << " " << static_cast<int>(myChar) << "\n";
        ++myChar;
    }
    
    cout << "\n===========================================\n\n";
    /*
     Affiche
     5 4 3 2 1
     4 3 2 1
     3 2 1
     2 1
     1
     */
    int row = 5;
    int column = 5;
    
    while (row >= 1)
    {
        column = row;
        while (column >= 1)
        {
            cout << column;
            --column;
        }
        cout << "\n";
        --row;
    }
    
    cout << "\n\n";
    
    cout << "\n===========================================\n\n";
    
    /*
     Affiche
             1
           2 1
         3 2 1
       4 3 2 1
     5 4 3 2 1
     */
    
    // There are 5 rows, we can loop from 1 to 5
    int outer = 1;
    
    while (outer <= 5)
    {
        // Row elements appear in descending order, so start from 5 and loop through to 1
        int inner = 5;
        
        while (inner >= 1)
        {
            // The first number in any row is the same as the row number
            // So number should be printed only if it is <= the row number, space otherwise
            if (inner <= outer)
                cout << inner << " ";
            else
                cout << "  "; // extra spaces purely for formatting purpose
            
            --inner;
        }
        
        // A row has been printed, move to the next row
        cout << "\n";
        
        ++outer;
    }
    
    cout << "\n\n";
    
    
    
    return 0;
}
