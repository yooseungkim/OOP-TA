#include <iostream>

using namespace std;
class Rectangle
{
public:
    int width, height;
    Rectangle(int w, int h) : width(w), height(h) {}
    ~Rectangle(){};

    int getArea()
    {
        return width * height;
    }

    int getPerimeter()
    {
        return 2 * (width + height);
    }
};

class Cuboid : public Rectangle
{
public:
    int depth;
    Cuboid(int w, int h, int d) : Rectangle(w, h), depth(d) {}
    ~Cuboid(){};

    int volume()
    {
        return this->getArea() * depth;
    }

    int getArea()
    {
        return 2 * (this->getArea() + width * depth + height * depth);
    }
};
int main()
{
    Rectangle rectangle(3, 4);
    Cuboid cuboid(3, 4, 5);

    cout << "Area : " << rectangle.getArea() << endl;
    cout <<
}