#include <iostream>

using namespace std;

class Point
{
    int x;
    int y;

public:
    Point(int x, int y) : x(x), y(y){};
    void setX(int _x) { x = _x; };
    void setY(int _y) { y = _y; };
    void show()
    {
        cout << "X: " << x << ", Y: " << y << endl;
    };

    Point operator+(const Point &);
    Point operator+(const int);
    Point operator++();
};

int main()
{
    Point p1(1, 2);
    Point p2(3, 6);

    p1 = p1 + p2;
    p1.show();

    ++p1;
    p1.show();

    p1 = p1 + 3;
    p1.show();
};

Point Point::operator+(const Point &p)
{
    return Point(x + p.x, y + p.y);
}

Point Point::operator+(const int n)
{
    return Point(x + n, y + n);
}

Point Point::operator++()
{
    return Point(++x, ++y);
}