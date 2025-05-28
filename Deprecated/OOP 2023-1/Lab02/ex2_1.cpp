#include <iostream>
#include <cmath>
using namespace std;

inline double circleArea(double radius) // inline function definition
{
    return M_PI * radius * radius;
}

int main()
{
    double radius;
    cout << "Enter the radius of the circle: ";
    cin >> radius;

    cout << "The radius of the circle is " << circleArea(radius);
}