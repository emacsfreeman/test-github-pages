//
//  main.cpp
//  Quizz47
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

/*
 My solution

#include <iostream>

using namespace std;

struct Advertising
{
    int numberOfAdsSeen;
    double percentageOfAdsClicked;
    double moneyMadeByAdClicked;
};

double calculateMoneyMadeByDay(Advertising ads)
{
    return ads.numberOfAdsSeen * ads.percentageOfAdsClicked * ads.moneyMadeByAdClicked;
}

int main()
{
    Advertising myAds = { 10, 20.50f, 0.02f };
    cout << "Money made this day: $" << calculateMoneyMadeByDay(myAds) << endl;
    
    
    
    return 0;
}
 */

/* Their solution */

#include <iostream>

// First we need to define our Advertising struct
struct Advertising
{
    int adsShown;
    double clickThroughRatePercentage;
    double averageEarningsPerClick;
};

Advertising getAdvertising()
{
    Advertising temp;
    std::cout << "How many ads were shown today? ";
    std::cin >> temp.adsShown;
    std::cout << "What percentage of users clicked on the ads? ";
    std::cin >> temp.clickThroughRatePercentage;
    std::cout << "What was the average earnings per click? ";
    std::cin >> temp.averageEarningsPerClick;
    return temp;
}

void printAdvertising(Advertising ad)
{
    std::cout << "Number of ads shown: " << ad.adsShown << '\n';
    std::cout << "Click through rate: " << ad.clickThroughRatePercentage << '\n';
    std::cout << "Average earnings per click: $" << ad.averageEarningsPerClick << '\n';
    
    // The following line is split up to reduce the length
    // We need to divide ad.clickThroughRatePercentage by 100 because it's a percent of 100, not a multiplier
    std::cout << "Total Earnings: $" <<
    (ad.adsShown * ad.clickThroughRatePercentage / 100 * ad.averageEarningsPerClick) << '\n';
}

int main()
{
    // Declare an Advertising struct variable
    Advertising ad = getAdvertising();
    printAdvertising(ad);
    
    return 0;
}
