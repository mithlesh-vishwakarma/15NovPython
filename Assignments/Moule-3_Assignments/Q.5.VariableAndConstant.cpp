// 1. Variables and Constants
//  Write a C++ program that demonstrates the use of variables and constants.Create variables of    different data types and perform operations on them
//     Objective : Understand the difference between variables and constants.

#include <iostream>
using namespace std;
int main()
{
  // Variable declarations
  int intVar = 10;
  float floatVar = 5.5;
  char charVar = 'A';
  double doubleVar = 20.99;

  // Constant declaration
  const int constVar = 100;

  // Performing operations
  int sumInt = intVar + constVar;
  float sumFloat = floatVar + 2.5;
  double sumDouble = doubleVar + 10.01;

  // Displaying results
  cout << "Integer Variable: " << intVar << endl;
  cout << "Float Variable: " << floatVar << endl;
  cout << "Character Variable: " << charVar << endl;
  cout << "Double Variable: " << doubleVar << endl;
  cout << "Constant Variable: " << constVar << endl;
  cout << "Sum of Integer Variable and Constant: " << sumInt << endl;
  cout << "Sum of Float Variable and 2.5: " << sumFloat << endl;
  cout << "Sum of Double Variable and 10.01: " << sumDouble << endl;

  return 0;
}