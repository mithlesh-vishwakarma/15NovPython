// Simple Calculator Using Functions:
// Write a C++ program that defines functions for basic arithmetic operations (add,
// subtract, multiply, divide). The main function should call these based on user input.
// Objective: Practice defining and using functions in C++.

#include <iostream>
using namespace std;

double add(double a, double b)
{
  return a + b;
}

double subtract(double a, double b)
{
  return a - b;
}

double multiply(double a, double b)
{
  return a * b;
}

double divide(double a, double b)
{
  if (b != 0)
    return a / b;
  else
  {
    cout << "Error: Division by zero!";
    return 0;
  }
}
int main()
{
  double num1, num2;
  char operation;
  double result;

  cout << "Simple Calculator";
  cout << "Enter first number: ";
  cin >> num1;
  cout << "Enter second number: ";
  cin >> num2;
  cout << "Enter an operator (1. for (+), 2.for(-), 3.for (*) ,4.for (/)): ";
  cin >> operation;

  switch (operation)
  {
  case '1':
    result = add(num1, num2);
    break;
  case '2':
    result = subtract(num1, num2);
    break;
  case '3':
    result = multiply(num1, num2);
    break;
  case '4':
    result = divide(num1, num2);
    break;
  default:
    cout << "Invalid operator!";
  }

  cout << "Result: " << result;

  return 0;
}