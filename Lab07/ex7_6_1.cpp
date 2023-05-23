#include <iostream>
using namespace std;

class Weapon
{
public:
    virtual void load() = 0;
};

class Bomb : public Weapon
{
    void load()
    {
        cout << "Load bomb" << endl;
    }
};

class Gun : public Weapon
{
    void load()
    {
        cout << "Load gun" << endl;
    }
};

int main()
{
    Weapon *a[3];
    a[0] = new Gun();
    a[1] = new Gun();
    a[2] = new Bomb();

    for (int i = 0; i < 3; i++)
    {
        a[i]->load();
    }
    return 0;
}