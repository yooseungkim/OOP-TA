#include <iostream>
#include <cstring>
#include <typeinfo>
using namespace std;

class Cents
{
private:
    int m_cents;

public:
    Cents(int cents = 0)
    {
        m_cents = cents;
        cout << "cents : " << cents << endl;
    }
    int getCents() const { return m_cents; }
    int &getCents() { return m_cents; }

    friend Cents operator+(const Cents &lhs, const Cents &rhs)
    {
        return (lhs.m_cents + rhs.m_cents);
    }
};

int main()
{
    Cents cents1(6);
    Cents cents2(8);

    Cents sum;
    // add(cents1, cents2, sum);
    sum = cents1 + cents2;
    cout << typeid(sum).name() << endl;

    cout << sum.getCents() << endl;

    return 0;
}