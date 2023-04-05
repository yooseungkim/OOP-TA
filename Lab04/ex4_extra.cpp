#include <iostream>

using namespace std;

class Rectangle
{
    float width, height;

public:
    Rectangle(float w = 1, float h = 1)
    {
        setWidth(w);
        setHeight(h);
    }

    float getWidth() const { return width; }
    float getHeight() const { return height; }
    void setWidth(float w)
    {
        w = w > 0 ? w : 1;
        w = w < 20 ? w : 20;
        width = w;
    }
    void setHeight(float h)
    {
        h = h > 0 ? h : 1;
        h = h < 20 ? h : 20;
        height = h;
    }
    float area() const { return width * height; }
    float perimeter() const { return 2 * width + 2 * height; }
    void print() const
    {
        cout << "width : " << width << " height : " << height;
        cout << "perimeter : " << perimeter() << " area : " << area() << endl;
    }
};

int main()
{
    Rectangle a;
    Rectangle b(5, 4);
    Rectangle c;

    a.print();
    b.print();
    c.print();
}