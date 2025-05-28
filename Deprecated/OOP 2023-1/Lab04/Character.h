#ifndef CHARACTER_H
#define CHARACTER_H

#include <cstring>
#include <iostream>
class Character
{
public:
    std::string name;
    int x;
    int y;
    int hp;
    Character(std::string);
    void print();
    void setX(int amount);
};

#endif // CHARACTER_H