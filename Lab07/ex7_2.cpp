#include <iostream>
using namespace std;

class Point
{
private:
    int x;
    int y;

public:
    Point(int a = 0, int b = 0)
    {
        x = a;
        y = b;
    }
    void setX(int a) { x = a; }
    void setY(int b) { y = b; }
    void show() { cout << " x:" << x << '\t' << " y:" << y << endl; }

    Point operator+(const Point &);
    Point operator+(const int);
    Point operator++();
};

Point Point::operator+(const Point &rhs)
{
    int newX = this->x + rhs.x;
    int newY = this->y + rhs.y;
    return Point(newX, newY);
}

Point Point::operator+(const int a)
{
    int newX = this->x + a;
    int newY = this->y + a;
    return Point(newX, newY);
}

Point Point::operator++()
{
    Point temp;
    temp.x = ++x;
    temp.y = ++y;
    return temp;
}

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

    return 0;
}