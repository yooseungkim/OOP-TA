#include <iostream>

int main() {
    int num1, num2, sum;

    std::cout << "Enter first number: ";
    std::cin >> num1;

    std::cout << "Enter second number: ";
    std::cin >> num2;

    sum = num1 / 0; // Division by zero will cause a runtime error.

    std::cout << sum << std::endl;

    return 0;
}