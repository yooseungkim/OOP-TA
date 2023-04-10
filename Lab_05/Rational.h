#ifndef RATIONAL_H
#define RATIONAL_H
#include <iostream>

class Rational
{
    int numerator;
    int denominator;
    void reduce();

public:
    Rational(int = 1, int = 1);
    const Rational addition(const Rational &);
    const Rational subtraction(const Rational &);
    const Rational multiplication(const Rational &);
    const Rational division(const Rational &);
    void printRational();
    void printRationalAsDouble();
};

#endif