#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cout << "Number of integers : ";
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cout << "Enter an integer : ";
        cin >> v[i];
    }
    int max = v[0];
    int min = v[0];
    for (auto &i : v)
    {
        max = max > i ? max : i;
        min = min < i ? min : i;
    }

    cout << "Max : " << max << endl;
    cout << "Min : " << min << endl;

    return 0;
}