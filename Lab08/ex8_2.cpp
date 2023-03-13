#include <iostream>
using namespace std;

class Complex
{
    int real;
    int img;

public:
    Complex(int = 0, int = 0);

    friend Complex operator+(Complex &lhs, Complex &rhs)
    {
        return Complex(lhs.real + rhs.real, lhs.img + rhs.img);
    }

    friend Complex operator-(Complex &lhs, Complex &rhs)
    {
        return Complex(lhs.real - rhs.real, lhs.img - rhs.img);
    }

    friend Complex operator*(Complex &lhs, Complex &rhs)
    {
        return Complex(lhs.real * rhs.real - lhs.img * rhs.img, lhs.real * rhs.img + lhs.img * rhs.real);
    }

    friend ostream &operator<<(ostream &out, const Complex &c)
    {
        out << c.real << "+" << c.img << "i";
        return out;
    }
};

int main()
{
    Complex c1(1, 2), c2(2, 4);
    Complex c3 = c1 + c2;
    cout << c3 << endl;
    c3 = c1 - c2;
    cout << c3 << endl;
    c3 = c1 * c2;
    cout << c3 << endl;
}

Complex::Complex(int r, int i) : real(r), img(i){};