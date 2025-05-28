#include <iostream>
using std::cout;
using std::endl;

#include <iomanip>

using std::setw;

#include "ex1_1_savingsaccount.h"

int main()
{
    SavingsAccount saver1(2000.0), saver2(3000.0);

    SavingsAccount::modifyInterestRate(.03);

    cout << "\nOutput monthly balances for one year at .03"
         << "\nBalances: Saver 1 ";
    saver1.printBalance();
    cout << "\tSaver 2 ";
    saver2.printBalance();

    for (int month = 1; month <= 12; ++month)
    {
        saver1.calculateMonthlyInterest();
        saver2.calculateMonthlyInterest();

        cout << "\nMonth" << setw(3) << month << ": Saver 1 ";
        saver1.printBalance();
        cout << "\tSaver 2 ";
        saver2.printBalance();
    }

    SavingsAccount::modifyInterestRate(.04);
    saver1.calculateMonthlyInterest();
    saver2.calculateMonthlyInterest();
    cout << "\nAfter setting interest rate to .04"
         << "\nBalances: Saver 1 ";
    saver1.printBalance();
    cout << "\tSaver 2 ";
    saver2.printBalance();
    cout << endl;

    return 0;
}