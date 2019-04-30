#include <iostream>

int doubleNumber(int x)
{
    return 2 * x;
}

int main()
{
    int x{ 0 };
    std::cin >> x;
    std::cout << doubleNumber(x) << '\n';
    return 0;
}
