#include <iostream>

using std::cout;
using std::endl;

#include "Rational.h"

int main()
{
    Rational c(1, 3), d(7, 8), x;

    c.printRational();
    cout << " + ";
    d.printRational();
    x = c.addition(d);
    cout << " = ";
    x.printRational();
    cout << '\n';
    x.printRational();
    cout << " = ";
    x.printRationalAsDouble();
    cout << "\n\n";

    c.printRational();
    cout << " - ";
    d.printRational();
    x = c.subtraction(d);
    cout << " = ";
    x.printRational();
    cout << '\n';
    x.printRational();
    cout << " = ";
    x.printRationalAsDouble();
    cout << "\n\n";

    c.printRational();
    cout << " x ";
    d.printRational();
    x = c.multiplication(d);
    cout << " = ";
    x.printRational();
    cout << '\n';
    x.printRational();
    cout << " = ";
    x.printRationalAsDouble();
    cout << "\n\n";

    c.printRational();
    cout << " / ";
    d.printRational();
    x = c.division(d);
    cout << " = ";

    return 0;
