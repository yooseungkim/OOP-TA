#include <iostream>

using namespace std;

class Car
{
private:
    int num;
    double gas;

public:
    Car();
    void setCar(int n, double g);
    void show();
    friend ostream &operator<<(ostream &, const Car);
};

Car::Car()
{
    num = 0;
    gas = 0.0;
    cout << "Car is constructed\n";
}

void Car::setCar(int n, double g)
{
    num = n;
    gas = g;
}

ostream &operator<<(ostream &os, const Car car)
{
    os << "Car's number: " << car.num << '\t' << "Gass Amount: " << car.gas << endl;
    return os;
}

int main()
{
    Car myCar;
    myCar.setCar(1234, 75.5);
    cout << myCar;

    return 0;
}