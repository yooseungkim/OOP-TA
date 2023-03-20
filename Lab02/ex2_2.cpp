#include <iostream>

using namespace std;

int big(int, int);
int big(int *, int);

int main()
{
    int array[5] = {1, 9, -2, 8, 6};
    cout << big(2, 3) << endl;
    cout << big(array, 5) << endl;
}

int big(int a, int b)
{
    return a > b ? a : b;
}

int big(int *a, int size)
{
    int i = 0;
    int max;
    for (i = 0; i < size; i++)
    {
        max = a[i] > max ? a[i] : max;
    }

    return max;
}
