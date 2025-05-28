#include <iostream>
#include <limits>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    vector<int> fib(12);
    for (int i = 0; i < 12; i++)
        if (i == 0)
            continue;
        else if (i == 1)
            fib[i] = 1;
        else
            fib[i] = fib[i - 1] + fib[i - 2];
    for (auto &i : fib)
        i *= 10;

    for (const auto &i : fib)
        cout << i << " ";
    cout << endl;

    int max_number = numeric_limits<int>::min();

    for (const auto &i : fib)
        max_number = max(max_number, i);

    cout << max_number << endl;

    return 0;
}