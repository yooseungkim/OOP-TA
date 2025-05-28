#include <iostream>
#include <cmath>
using namespace std;
class Circle
{
public:
    int radius;
    Circle(int r) : radius(r) {}
    ~Circle(){};

    double getArea()
    {
        return M_PI * radius * radius;
    }

    double getPerimeter()
    {
        return 2 * M_PI * radius;
    }
};

class Sphere : public Circle
{
public:
    Sphere(int r) : Circle(r) {}
    ~Sphere(){};

    double getVolume()
    {
        return (4.0 / 3) * radius * getArea();
    }

    double getSurface()
    {
        return 2 * radius * getPerimeter();
    }
};
int main()
{
    Circle circle(5);
    Sphere sphere(5);

    cout << "Area : " << circle.getArea() << endl;
    cout << "Perimeter : " << circle.getPerimeter() << endl;
    cout << "Surface Area : " << sphere.getSurface() << endl;
    cout << "Volume : " << sphere.getVolume() << endl;
}