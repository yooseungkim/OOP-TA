#include "Complex.h"

using namespace std;

int main()
{
    Complex b(1, 7), c(9, 2);
    b.printComplex();
    cout << " + ";
    c.printComplex();
    b.addition(c);
    cout << " = ";
    b.printComplex();

    cout << endl;
}