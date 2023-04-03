#include "Complex.h"

Complex::Complex(double re, double im) : re(re), im(im){};

void Complex::printComplex()
{
    std::cout << "(" << re << ", " << im << ")";
};

void Complex::addition(const Complex c)
{
    re += c.re;
    im += c.im;
}

void Complex::subtraction(const Complex c)
{
    re -= c.re;
    im -= c.im;
}

void Complex::initialize(double re, double im)
{
    this->re = re;
    this->im = im;
}
