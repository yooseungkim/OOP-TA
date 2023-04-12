#include <iostream>

using namespace std;

class Point
{
    int x;
    int y;

public:
    Point(int x = 0, int y = 0) : x(x), y(y){};
    void setX(int x) { this->x = x; };
    void setY(int y) { this->y = y; };
    void show()
    {
        cout << "x : " << x << " y : " << y << endl;
    }

    friend Point operator+(const Point &p1, const Point &p2);
    friend Point operator+(int, const Point &rhs);
    friend Point operator+(const Point &lhs, int);
};
Point operator+(const Point &p1, const Point &p2)
{
    Point temp(p1.x + p2.x, p1.y + p2.y);
    return temp;
}

Point operator+(int a, const Point &rhs)
{
    Point temp(rhs.x + a, rhs.y + a);
    return temp;
}
Point operator+(const Point &lhs, int a)
{
    Point temp(lhs.x + a, lhs.y + a);
    return temp;
}

int main()
{
    Point p1(1, 2);
    Point p2(2, 3);

    p1.show();
    p2.show();

    Point p3;
    p3 = p1 + p2;
    Point p4;
    p3.show();
    p4 = 3 + p1;
    p4.show();
    p4 = p1 + 3;
    p4.show();
    return 0;
}