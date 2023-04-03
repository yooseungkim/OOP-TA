#include <iostream>

using namespace std;

class Complex
{
    int real;
    int imag;
    void init(int r, int i)
    {
        real = r;
        imag = i;
    }

public:
    void init(int r, int i);
    void print()
    {
        if (imag >= 0)
        {
            cout << real << " + " << imag << "i" << endl;
        }

        else
        {
            cout << real << " - " << -imag << "i" << endl;
        }
    }
};

int main()
{
    Complex obj;
    obj.init(1, 2);
    obj.print();

    Complex b;
    b.init(3, -4);
    b.print();
}