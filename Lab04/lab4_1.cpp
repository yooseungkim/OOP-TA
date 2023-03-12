#include <iostream>
using namespace std;

void tripleByReference(int &); // call by reference, copying address of int n

int main()
{
    cout << "Enter an integer: ";
    int n;
    cin >> n;
    tripleByReference(n); // passes address of n;
    cout << "Value (in main) after call to tripleByReference() is : " << n << endl;
}

void tripleByReference(int &n)
{
    n *= 3;
}