#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    srand(static_cast<unsigned int>(time(0)));
    unsigned int arr[10] = {0};
    for (int i = 0; i < 10; i++)
    {
        arr[i] = rand() % 100 + 1;
    }

    int max = arr[0];
    for (int i = 1; i < 10; i++)
    {
        cout << arr[i] << " ";
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    cout << endl
         << max << endl;

    return 0;
}