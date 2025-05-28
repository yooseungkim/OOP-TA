#include <iostream>

using namespace std;

template <typename T>
T getAverage(T array[], int len)
{
    T sum = 0;
    for (int i = 0; i < len; i++)
    {
        sum += array[i];
    }
    return sum / len;
}

int main()
{
    double list[] = {1.2, 3.3, 9.0, 1.5, 8.7};
    cout << "Average : " << getAverage(list, 5) << endl;

    return 0;
}