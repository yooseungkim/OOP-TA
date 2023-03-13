#include <iostream>
using namespace std;

class abc
{
    int a;

public:
    void init();
    friend void print(abc);
};

void abc::init()
{
    a = 10;
}

// 2. Friend function definition
void print(abc a)
{
    cout << "Value : " << a.a << endl;
}

int main()
{
    abc k;

    k.init();
    print(k);

    return 0;
}