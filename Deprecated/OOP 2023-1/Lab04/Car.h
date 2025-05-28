#ifndef CAR_H
#define CAR_H

#include<iostream>
#include<string>
using namespace std;

class Car
{
    int speed;
    int gear;
    string color;
public:
    Car(int init); 
    ~Car();
    int getSpeed();
    void setSpeed(int s);
};

#endif // CAR_H