//
//  main.cpp
//  Array2
//
//  Created by Laurent Garnier on 01/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int numberOfCars = 3;
    int carMiles[] = {15, 13, 15};
    string carManufacturers[] = {"Saab", "Volvo", "BMW"};
    
    for (int i = 0; i < 3; i++)
    {
        if (i == 2)
        {
            cout << carManufacturers[i] << ": " << carMiles[i] << ".\n";
        }
        else
        {
            cout << carManufacturers[i] << ": " << carMiles[i] << ", ";
        }
        
    }
    
    
    cout << "Number of cars: " << numberOfCars << endl;
    
    return 0;
}
