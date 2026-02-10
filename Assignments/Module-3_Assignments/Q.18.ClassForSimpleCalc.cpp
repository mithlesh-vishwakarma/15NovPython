// Class for a Simple Calculator
// Write a C++ program that defines a class Calculator with functions for addition,
// subtraction, multiplication, and division. Create objects to use these functions.
// Objective: Introduce basic class structure.

#include <iostream>
using namespace std;
class Calculator
{
public:
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
    {
      return a / b;
    }
    else
    {
      cout << "Error: Division by zero!";
      return 0;
    }
  }
};
int main()
{
  Calculator calc;

  double num1, num2;
  cout << "Enter two numbers: ";
  cin >> num1 >> num2;

  cout << "Addition: " << calc.add(num1, num2) << endl;
  cout << "Subtraction: " << calc.subtract(num1, num2) << endl;
  cout << "Multiplication: " << calc.multiply(num1, num2) << endl;
  cout << "Division: " << calc.divide(num1, num2) << endl;

  return 0;
}