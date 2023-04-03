#include "Character.h"

Character::Character(std::string name)
{
    this->name = name;
    this->hp = 100;
    this->x = 0;
    this->y = 0;
};

void Character::print()
{
    std::cout << "x: " << x << " y: " << y << " HP: " << hp << std::endl;
};

void Character::setX(int x)
{
    this->x = x;
}