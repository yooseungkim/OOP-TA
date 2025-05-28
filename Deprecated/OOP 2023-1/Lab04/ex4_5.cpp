#include "Character.h"

using namespace std;

int main()
{
    cout << "Character name : ";
    string name;
    cin >> name;

    Character c(name);
    for (int i = 0; i < 10; i++)
    {
        c.setX(i * 10);
        c.print();
    }

    return 0;
}