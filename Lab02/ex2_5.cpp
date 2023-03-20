#include <iostream>

using namespace std;

int getMax(int x, int y) // opt + shift + arrow
{
    return x > y ? x : y;
}
double getMax(double x, double y)
{
    return x > y ? x : y;
}
float getMax(float x, float y)
{
    return x > y ? x : y;
}
char getMax(char x, char y)
{
    return x > y ? x : y;
}

int main()
{
    cout << getMax(1, 2) << endl;
    cout << getMax(3.14, 1.592) << endl;
    cout << getMax(1.0f, 3.4f) << endl;
    cout << getMax('a', 'c') << endl;
}
