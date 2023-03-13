#include <iostream>

using namespace std;

class CoffeeMachine
{
    int coffee;
    int sugar;
    int water;

public:
    CoffeeMachine(int, int, int);
    void drinkEspresso();
    void drinkAmericano();
    void drinkSugarCoffee();
    void show();
    void fill();
};

int main()
{
    CoffeeMachine java(5, 10, 3);
    java.drinkEspresso();
    java.show();
    java.drinkAmericano();
    java.show();
    java.drinkSugarCoffee();
    java.show();
    java.fill();
    java.show();
    return 0;
}

CoffeeMachine::CoffeeMachine(int c, int w, int s) : coffee(c), water(w), sugar(s){};

void CoffeeMachine::drinkAmericano()
{
    if (water >= 2 and coffee >= 1)
    {
        water -= 2;
        coffee -= 1;
    }
};

void CoffeeMachine::drinkEspresso()
{
    if (water >= 1 and coffee >= 1)
    {
        water -= 1;
        coffee -= 1;
    }
};

void CoffeeMachine::drinkSugarCoffee()
{
    if (water >= 2 and coffee >= 1 and sugar >= 1)
    {
        water -= 2;
        coffee -= 1;
        sugar -= 1;
    }
}

void CoffeeMachine::fill()
{
    water = 10;
    coffee = 10;
    sugar = 10;
}

void CoffeeMachine::show()
{
    cout << "Material Output, Coffee : " << coffee
         << ", Water : " << water << ", Sugar : " << sugar << endl;
}