#include <iostream>
using namespace std;

class Oval
{
    int width;
    int height;

public:
    Oval(int = 1, int = 1);
    ~Oval();
    void set(int, int);
    int getHeight();
    int getWidth();
    void show();
};

int main()
{
    Oval a, b(3, 4);
    a.set(10, 20);
    a.show();
    cout << b.getWidth() << ", " << b.getHeight() << endl;
    return 0;
}

Oval::Oval(int w, int h) : width(w), height(h) {}
Oval::~Oval()
{
    show();
}

void Oval::set(int w, int h)
{
    width = w;
    height = h;
}

void Oval::show()
{
    cout << "width: " << width << ", height: " << height << endl;
}

int Oval::getHeight()
{
    return height;
}

int Oval::getWidth()
{
    return width;
}