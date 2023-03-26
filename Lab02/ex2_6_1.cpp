#include <iostream>

using namespace std;

int sum(int a, int b)
{
    int answer = 0;
    for (int i = a; i <= b; i++)
    {
        answer += i;
    }
    return answer;
}

int sum(int a)
{
    return sum(0, a);
}

int main()
{
    cout << sum(3, 5) << endl;
    cout << sum(10, 15) << endl;
    cout << sum(100) << endl;
}