#ifndef COMPLEX_H
#define COMPLEX_H

#include <iostream>
class Complex
{
    double re;
    double im;

public:
    Complex(double = 0, double = 0);
    void printComplex();
    void addition(const Complex);
    void subtraction(const Complex);
    void initialize(double, double);
};

#endif