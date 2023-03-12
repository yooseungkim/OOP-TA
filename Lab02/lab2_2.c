#include <stdio.h>
#include <math.h>
typedef struct complex
{
    double real;
    double imaginary;
} Complex;

double CMag(Complex x)
{
    // return sqrt(x.real * x.real + x.imaginary * x.imaginary);
    return sqrt(pow(x.real, 2) + pow(x.imaginary, 2));
}

int main()
{
    Complex array[10];
    printf("Enter 10 complex numbers: ");
    int i = 0;
    for (; i < 10; i++)
    {
        double x, y;
        scanf("%lf %lf", &x, &y);
        Complex z = {x, y};
        array[i] = z;
    }
    double key;
    printf("Enter a magnitude search key: ");
    scanf("%lf", &key);
    for (i = 0; i < 10; i++)
    {
        if (key == CMag(array[i]))
        {
            printf("The complex number with magnitude %lf is found at position %d", key, i);
            printf("The complex nubmer is %lf + %lfi", array[i].real, array[i].imaginary);
            return 0;
        }
    }
    printf("The search key cannot be found");
    return 0;
}