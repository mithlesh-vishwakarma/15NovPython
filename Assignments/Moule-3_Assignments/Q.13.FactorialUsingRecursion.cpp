// Factorial Calculation Using Recursion : Write a C++ program that calculates the factorial of a number using recursion.
// Objective : Understand recursion in functions.

#include <iostream>
using namespace std;
unsigned long long factorial(int n)
{
  if (n == 0 || n == 1)
    return 1;
  else
    return n * factorial(n - 1);
}
int main()
{
  int number;

  cout << "Enter a positive integer to calculate its factorial: ";
  cin >> number;

  if (number < 0)
  {
    cout << "Error: Factorial is not defined for negative numbers.";
  }

  unsigned long long result = factorial(number);
  cout << "The factorial of " << number << " is: " << result;

  return 0;
}