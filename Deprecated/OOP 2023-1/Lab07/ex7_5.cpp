#include <iostream>
#include <cmath>
using namespace std;

class Shape
{
protected:
    int x, y;

public:
    Shape(int x, int y) : x(x), y(y){};
    virtual double getArea() = 0;
};

class Rect : public Shape
{
    int width, height;

public:
    Rect(int x, int y, int h, int w) : Shape(x, y), width(w), height(h){};
    double getArea()
    {
        return width * height;
    }
};

class Triangle : public Shape
{
    int width, height;

public:
    Triangle(int x, int y, int h, int w) : Shape(x, y), width(w), height(h){};
    double getArea()
    {
        return width * height / 2;
    }
};

class Circle : public Shape
{
    int radius;

public:
    Circle(int x, int y, int r) : Shape(x, y), radius(r){};
    double getArea()
    {
        return M_PI * radius * radius;
    }
};

int main()
{
    Shape *shapes[3];
    shapes[0] = new Rect(10, 10, 30, 40);
    shapes[1] = new Circle(5, -5, 20);
    shapes[2] = new Triangle(-5, -5, 50, 60);

    for (int i = 0; i < 3; i++)
    {
        cout << shapes[i]->getArea() << endl;
    }
}