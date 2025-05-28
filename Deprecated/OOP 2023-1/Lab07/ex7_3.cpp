#include <iostream>
#include <cmath>
using namespace std;

class Circle
{
    int radius;

public:
    Circle(int r) : radius(r){};
    ~Circle(){};

    double getPeri()
    {
        return 2 * M_PI * radius;
    }

    double getArea()
    {
        return M_PI * radius * radius;
    }
};

class Cylinder : public Circle
{
    int height;

public:
    Cylinder(int r, int h) : Circle(r), height(h){};
    ~Cylinder(){};

    double getSurface()
    {
        return 2 * getArea() + getPeri() * height;
    }

    double getVolume()
    {
        return getArea() * height;
    }
};

int main()
{
    Circle circle(5);
    Cylinder cylinder(5, 10);

    cout << circle.getPeri() << endl;
    cout << circle.getArea() << endl;
    cout << cylinder.getSurface() << endl;
    cout << cylinder.getVolume() << endl;
}
