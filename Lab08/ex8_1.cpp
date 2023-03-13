#include <iostream>
using namespace std;

class Complex
{

public:
    int real;
    int img;
    Complex(int = 0, int = 0);

    Complex operator+(Complex &rhs)
    {
        return Complex(real + rhs.real, img + rhs.img);
    }

    Complex operator-(Complex &rhs)
    {
        return Complex(real - rhs.real, img - rhs.img);
    }

    Complex operator*(Complex &rhs)
    {
        return Complex(real * rhs.real - img * rhs.img, real * rhs.img + img * rhs.real);
    }
};

int main()
{
    Complex c1(1, 2), c2(2, 4);
    Complex c3 = c1 + c2;
    cout << c3.real << "+i" << c3.img << endl;
    c3 = c1 - c2;
    cout << c3.real << "+i" << c3.img << endl;
    c3 = c1 * c2;
    cout << c3.real << "+i" << c3.img << endl;
}

Complex::Complex(int r, int i) : real(r), img(i){};