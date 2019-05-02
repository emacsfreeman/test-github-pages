//
//  main.cpp
//  Game1
//
//  Created by Laurent Garnier on 02/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int numberSelected = 0;
    cout << "Player 1, pick up a number between 0 and 100 : ";
    cin >> numberSelected;
    
    int numberOfTry = 0;
    int guess = numberSelected + 1;
    while (guess != numberSelected)
    {
        cout << "Player 2, try to guess the number selected by Player 1 between 0 and 100 : ";
        cin >> guess;
        numberOfTry++;
        
        if (guess == numberSelected)
            cout << "\nCONGRATULATIONS! You find it! In " << numberOfTry << " times\n";
        else
        {
            if (guess < numberSelected)
                cout << "WRONG! It's greater.\n";
            else if (guess > numberSelected)
                cout << "WRONG! It's lower.\n";
        }
    }
    
    // Ivan version
    int currentGuess = 0;
    int theNumberToGuess = 0;
    cout << "Welcome to the game" << endl << endl;
    cout << "Player One: Please select a number: " << endl;
    cin >> theNumberToGuess;
    
    while (true)
    {
        
        cout << "Player 2, please guess the number: " << endl;
        cin >> currentGuess;
        
        if (currentGuess > theNumberToGuess)
            cout << "TOO HIGH! Guess lower!" << endl;
        else if (currentGuess < theNumberToGuess)
            cout << "TOO LOW! Guess higher!" << endl;
        else
        {
            cout << "YOU GUESSED CORRECTLY!!!!";
            break;
        }
    }
}
