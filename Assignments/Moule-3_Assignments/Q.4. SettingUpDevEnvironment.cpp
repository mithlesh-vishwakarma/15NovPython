// 4. Setting Up Development Environment :
// Write a program that asks for two numbers and displays their sum. Ensure this is done after setting up the IDE (like Dev C++ or CodeBlocks).
// Objective: Help students understand how to install, configure, and run programs in an IDE.

#include <iostream>
using namespace std;

int main()
{
  float num1, num2, sum;

  // Accept user input
  cout << "Enter first number: ";
  cin >> num1;
  cout << "Enter second number: ";
  cin >> num2;

  // Calculate sum
  sum = num1 + num2;

  // Display the result
  cout << "\nThe sum of " << num1 << " and " << num2 << " is: " << sum;

  return 0;
}