#include <iostream>
#include <string>
#include "Car.h"
using namespace std;

int main()
{
    Car myCar(0);
    cout << "Current speed: " << myCar.getSpeed() << endl;

    myCar.setSpeed(90);
    cout << "Current speed: " << myCar.getSpeed() << endl;

    return 0;
}