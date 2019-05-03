//
//  main.cpp
//  TemplateClassesTypedef
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

using namespace std;

template <class T>
class MathTools
{
public:
    T multiply(T a, T b)
    {
        return a * b;
    }
    T divide(T a, T b)
    {
        return a / b;
    }
    T add(T a, T b)
    {
        return a + b;
    }
    T subtraction(T a, T b)
    {
        return a - b;
    }
};

typedef MathTools<int> IntTools;
typedef MathTools<double> DoubleTools;

int main()
{
    IntTools intMathTools;
    DoubleTools doubleMathTools;
    cout << intMathTools.add(3.3, 2) << endl;
    cout << doubleMathTools.add(3.3, 2) << endl;
    return 0;
}
