#include <iostream>

int main() {
    int num1, num2, sum;

    std::cout << "Enter first number: ";
    std::cin >> num1;

    std::cout << "Enter second number: ";
    std::cin >> num2;

    sum = num1 + num2;

    std::cout << "The sum is: " << sum << std::endl;

    return 0;
}