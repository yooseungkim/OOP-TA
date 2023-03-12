#include <stdio.h>

typedef struct complex
{
    double real;
    double imaginary;
} Complex;

Complex CAdd(Complex, Complex);
Complex CSub(Complex, Complex);
Complex CMul(Complex, Complex);
Complex CDiv(Complex, Complex);
double CMag(Complex);

int main()
{
    double x, y;
    printf("Enter a first complex number: ");
    scanf("%lf %lf", &x, &y);
    Complex c1 = {x, y};
    printf("Enter a second complex number: ");
    scanf("%lf %lf", &x, &y);
    Complex c2 = {x, y};
    int sel;
    printf("(1) Add (2) Sub (3) Mul (4) Div\n");
    printf("Which operation do you want ");
    scanf("%d", &sel);
    Complex c3;
    switch (sel)
    {
    case 1:
        c3 = CAdd(c1, c2);
        break;
    case 2:
        c3 = CSub(c1, c2);
        break;
    case 3:
        c3 = CMul(c1, c2);
        break;
    case 4:
        c3 = CDiv(c1, c2);
        break;
    default:
        printf("Invalid Operation\n");
        break;
    }
    printf("Result: %lf+i%lf\n", c3.real, c3.imaginary);
    return 0;
}

Complex CAdd(Complex x, Complex y)
{
    Complex z = {x.real + y.real, x.imaginary + y.imaginary};
    return z;
}

Complex CSub(Complex x, Complex y)
{
    Complex z = {x.real - y.real, x.imaginary - y.imaginary};
    return z;
}

Complex CMul(Complex x, Complex y)
{
    double real = x.real * y.real - x.imaginary * y.imaginary;
    double imaginary = x.imaginary * y.real + x.real * y.imaginary;
    Complex z = {real, imaginary};
    return z;
}

Complex CDiv(Complex x, Complex y)
{
    if (CMag(y))
    {
        double real = (x.real * y.real + x.imaginary * y.imaginary) / CMag(y);
        double imaginary = (x.imaginary * y.real - x.real * y.imaginary) / CMag(y);
        Complex z = {real, imaginary};
        return z;
    }
    else
    {
        Complex z = {0, 0};
        return z;
    }
}

double CMag(Complex x)
{
    return x.real * x.real + x.imaginary * x.imaginary;
}