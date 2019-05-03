//
//  main.cpp
//  ClassesUsedWithoutKnowingIt
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <string>
#include <array>
#include <vector>
#include <iostream>

int main()
{
    std::string s { "Hello, world!" }; // instantiate a string class object
    std::array<int, 3> a { 1, 2, 3 }; // instantiate an array class object
    std::vector<double> v { 1.1, 2.2, 3.3 }; // instantiate a vector class object
    
    std::cout <<"\"" << s << "\" is a string with a length of: " << s.length() << '\n'; // call a member function
    
    for (int count = 0; count < 3; count++)
    {
        std::cout << "In the array a at index " << count << " we have: " << a[count] << "\n";
    }
    
    return 0;
}
