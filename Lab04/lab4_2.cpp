#include <iostream>

using namespace std;

template <typename T>
void minimum(T, T);

int main()
{
    minimum(7, 54);
    minimum(4.35, 8.46);
    minimum('g', 'T');

    return 0;
}

template <typename T>
void minimum(T x, T y)
{
    T min = x < y ? x : y;
    T max = x > y ? x : y;
    cout << min << " is smaller than " << max << endl;
}