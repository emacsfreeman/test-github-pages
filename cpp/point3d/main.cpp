//
//  main.cpp
//  Point3d
//
//  Created by Laurent Garnier on 02/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

struct Point3d
{
    double x;
    double y;
    double z;
};

Point3d getZeroPoint()
{
    Point3d temp = { 0.0, 0.0, 0.0 };
    return temp;
}

int main()
{
    Point3d zero = getZeroPoint();
    
    if (zero.x == 0.0 && zero.y == 0.0 && zero.z == 0.0)
        cout << "The point is zero\n";
    else
        cout << "The point is not zero\n";
    return 0;
}
