#include <iostream>

using namespace std;

class Car
{
    int num;
    int gas;

public:
    Car() : num(0), gas(0) { cout << "Constructed" << endl; };
    void setCar(int n, int g)
    {
        num = n;
        gas = g;
    };

    friend ostream &operator<<(ostream &out, const Car &car)
    {
        out << "num : " << car.num << ", gas : " << car.gas;
        return out; // for cascading
    };
};

int main()
{
    Car myCar;
    myCar.setCar(10, 20);
    cout << myCar << endl;
    return 0;
}