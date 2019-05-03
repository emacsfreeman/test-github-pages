//
//  main.cpp
//  Namespaces
//
//  Created by Laurent Garnier on 03/05/2019.
//  Copyright © 2019 Laurent Garnier. All rights reserved.
//

#include <iostream>

namespace awesomeNamespace
{
    void greetings()
    {
        std::cout << "Greetings from awesome namespace" << std::endl;
    }
}

using namespace awesomeNamespace;


int main()
{
    awesomeNamespace::greetings();
    greetings();
    
    return 0;
}

