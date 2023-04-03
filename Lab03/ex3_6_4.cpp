#include <iostream>
#include <string>
using namespace std;

class BankAccount
{
    string accountNumber;
    int balance;

public:
    void init(string accountNumber, int balance)
    {
        this->accountNumber = accountNumber;
        this->balance = balance;
    };

    void withdraw(int amount)
    {
        this->balance -= amount;
    }

    void deposit(int amount)
    {
        this->balance += amount;
    }

    int getBalance()
    {
        return balance;
    }
};

int main()
{
    BankAccount obj;

    obj.init("123456789", 100000);
    cout << "Current balance: " << obj.getBalance() << endl;
    obj.deposit(10000);
    cout << "After deposit: " << obj.getBalance() << endl;
    obj.withdraw(1000);
    cout << "After withdraw: " << obj.getBalance() << endl;
}