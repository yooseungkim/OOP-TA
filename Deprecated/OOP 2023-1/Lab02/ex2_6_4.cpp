#include <iostream>

using namespace std;

int tripleByValue(int n)
{
    return n * 3;
}

int tripleByReference(int &n)
{
    n *= 3;
    return n;
}

int main()
{
    int n;
    cout << "Enter an integer : ";
    cin >> n;

    cout << "Value before call to tripleCallByValue() is : " << n << endl;
    cout << "Value returned by tripleCallByValue() is : " << tripleByValue(n) << endl;
    cout << "Value (in main) after tripleCallByValue() is : " << n << endl;

    cout << "Value before call to tripleCallByReference() : " << n << endl;
    tripleByReference(n);
    cout << "Value (in main) after tripleCallByReference() is : " << n << endl;
}