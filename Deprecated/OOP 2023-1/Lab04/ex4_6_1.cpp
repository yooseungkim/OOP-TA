#include <iostream>

using namespace std;

class Box
{
public:
    int h;
    int w;
    char c;
    Box(int h, int w, char c = '*') : h(h), w(w), c(c){};
    void draw()
    {
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                cout << c;
            }
            cout << endl;
        }
        cout << endl;
    }
};

int main()
{
    Box b(2, 10);
    b.draw();
    Box b2(5, 6, '^');
    b2.draw();

    return 0;
}