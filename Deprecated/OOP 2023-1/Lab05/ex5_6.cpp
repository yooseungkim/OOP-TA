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

    Point operator+(const Point &other)
    {
        Point temp(this->x + other.x, this->y + other.y);
        return temp;
    }

    friend Point operator-(const Point &lhs, const Point &rhs);
};

Point operator-(const Point &lhs, const Point &rhs)
{
    Point temp(lhs.x - rhs.x, lhs.y - rhs.y);
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
    p4 = p1 - p2;

    p3.show();
    p4.show();
    return 0;
}