#include "SavingsAccount.h"

double SavingsAccount::annualInterestRate;

SavingsAccount::SavingsAccount(double amount)
{
    this->savingsBalance = amount;
}

void SavingsAccount::printBalance()
{
    std::cout << "Savings balance: " << this->savingsBalance << std::endl;
}

void SavingsAccount::modifyInterestRate(double interestRate)
{
    SavingsAccount::annualInterestRate = interestRate;
}

void SavingsAccount::calculateMonthlyInterest()
{
    this->savingsBalance += this->savingsBalance * SavingsAccount::annualInterestRate / 12;
}
