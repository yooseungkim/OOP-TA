#include "Rational.h"

void Rational::reduce()
{
    int sign = 1;
    if (numerator > 0 && denominator < 0)
    {
        denominator *= -1;
        sign = -1;
    }
    else if (denominator > 0 && numerator < 0)
    {
        numerator *= -1;
        sign = -1;
    }
    else if (denominator < 0 && numerator < 0)
    {
        numerator *= -1;
        denominator *= -1;
    }
    int gcd = 1;
    int i = 2;
    while (gcd <= (numerator > denominator ? denominator : numerator) && i <= (numerator > denominator ? denominator : numerator))
    {
        if ((numerator / gcd) % i == 0 && (denominator / gcd) % i == 0)
        {
            gcd *= i;
        }
        else
        {
            i++;
        }
    }
    this->numerator = (sign * numerator) / gcd;
    this->denominator = denominator / gcd;
};

Rational::Rational(int num, int denom)
{
    numerator = num;
    denominator = denom;
    this->reduce();
};

const Rational Rational::addition(const Rational &a)
{
    const Rational temp(this->numerator * a.denominator + this->denominator * a.numerator,
                        this->denominator * a.denominator);
    return temp;
};

const Rational Rational::subtraction(const Rational &a)
{
    const Rational temp(this->numerator * a.denominator - this->denominator * a.numerator,
                        this->denominator * a.denominator);
    return temp;
};

const Rational Rational::multiplication(const Rational &a)
{
    const Rational temp(this->numerator * a.numerator,
                        this->denominator * a.denominator);
    return temp;
};

const Rational Rational::division(const Rational &a)
{
    const Rational temp(this->numerator * a.denominator,
                        this->denominator * a.numerator);
    return temp;
};

void Rational::printRational()
{
    std::cout << numerator << "/" << denominator;
};

void Rational::printRationalAsDouble()
{
    std::cout << ((double)numerator) / denominator;
}
