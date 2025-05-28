#include <iostream>
#include <cstdarg>

using namespace std;

int sum(int, int);
int sum(int, int, int);
int sum(int, int, int, int);
int sum_args(int, ...);

int main()
{
    cout << sum(10, 15) << endl;
    cout << sum(10, 15, 25, 30) << endl;
    cout << sum(10, 15, 25) << endl;
    cout << sum_args(2, 10, 15) << endl;
    cout << sum_args(3, 10, 15, 25) << endl;
    cout << sum_args(4, 10, 15, 25, 30) << endl;
}

int sum(int a, int b)
{
    return a + b;
}

int sum(int a, int b, int c)
{
    return a + b + c;
}

int sum(int a, int b, int c, int d)
{
    return a + b + c + d;
}

int sum_args(int args, ...)
{
    va_list ap;
    va_start(ap, args);
    int answer = 0;
    int i = 0;
    for (i = 0; i < args; i++)
    {
        answer += va_arg(ap, int);
    }

    return answer;
}