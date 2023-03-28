#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> v(0);
    int n = 1;
    while (n > 0)
    {
        cout << "Enter a grade (exit = -1) : ";
        cin >> n;
        if (n == -1)
        {
            break;
        }
        v.resize(v.size() + 1, n);
    }

    int sum = 0;
    for (const auto &i : v)
    {
        sum += i;
    }
    cout << "Average : " << sum / v.size() << endl;

    return 0;
}