#ifndef SAVINGS_ACCOUNT_H
#define SAVINGS_ACCOUNT_H

#include <iostream>

class SavingsAccount
{
    static double annualInterestRate;
    double savingsBalance;

public:
    SavingsAccount(double);
    void printBalance();
    void calculateMonthlyInterest();
    static void modifyInterestRate(double);
};

#endif