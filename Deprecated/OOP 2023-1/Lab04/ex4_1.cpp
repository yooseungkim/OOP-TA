#include <iostream>
using namespace std;

class Rectangle
{
    int height;
    int width;

public:
    Rectangle(int h, int w);
    int calcArea();
};

int main()
{
    Rectangle r(3, 4); // r{3,4} is c++11 standard
    cout << "Area of Rectangle : " << r.calcArea() << endl;
    return 0;
}

Rectangle::Rectangle(int h, int w)
{
    height = h;
    width = w;
}

int Rectangle::calcArea()
{
    return height * width;
}