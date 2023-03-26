#include <iostream>

using namespace std;

template <typename T>
T getSmallest(T array[], int len)
{
    T min = array[0];
    for (int i = 0; i < len; i++)
    {
        min = min < array[i] ? min : array[i];
    }

    return min;
}

int main()
{
    double list[] = {1.2, 3.3, 9.0, 1.5, 8.7};
    cout << "Minimum: " << getSmallest(list, 5) << endl;

    return 0;
}