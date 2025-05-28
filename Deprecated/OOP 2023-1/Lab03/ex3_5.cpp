#include <iostream>
#include <string>

using namespace std;

class Friend
{
    string name;
    string address;
    int age;
    double weight;
    double height;

public:
    Friend(string name, string address, int age, double weight, double height) : name(name), address(address), age(age), weight(weight), height(height){};
    friend void print(const Friend &fr);
};

void print(const Friend &fr)
{
    cout << fr.name << " " << fr.address << " " << fr.age << " " << fr.weight << " " << fr.height << endl;
}

int main()
{
    Friend ele = Friend("Gil Dong Hong",
                        "Jangseong",
                        20,
                        175,
                        72);
    print(ele);
    return 0;
}
