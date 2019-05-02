//
//  main.cpp
//  Loops
//
//  Created by Laurent Garnier on 02/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int numberOfCars = 3;
    int carMiles[] = {15, 13, 15};
    
    // total of Miles
    int totalMiles = 0;
    for (int counter = 0; counter < numberOfCars; counter++)
    {
        cout << "Counter is now " << counter << endl;
        cout << "carMiles[counter] is now  " << carMiles[counter] << endl;
        
        totalMiles += carMiles[counter];
    }
    
    cout << "Total miles of all cars is " << totalMiles << endl;
    
    return 0;
}
