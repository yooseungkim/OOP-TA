#include "Car.h"
#include <iostream> 
Car::Car(int init)
    : speed(init)
{
    cout << "Constructor called " << endl;
}
Car::~Car()
{
    cout << "Destructor called " << endl;
}
int Car::getSpeed()
{
    return speed;
}

void Car::setSpeed(int s)
{
    speed = s;
}
