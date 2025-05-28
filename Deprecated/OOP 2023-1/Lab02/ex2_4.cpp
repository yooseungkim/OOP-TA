#include <iostream>
#include <cmath>
using namespace std;

void getSinCos(double degree, double &s, double &c)
{
    s = sin(degree * M_PI / 180); // degree to radian
    c = cos(degree * M_PI / 180);
}

int main()
{
    double sin = 0.0;
    double cos = 0.0;

    getSinCos(30.0, sin, cos);
    cout << sin << " " << cos << endl;
}