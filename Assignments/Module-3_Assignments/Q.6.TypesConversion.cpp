// 2. Type Conversion
//   Write a C++ program that performs both implicit and explicit type conversions and prints the results
//   Objective : Practice type casting in C++.

#include <iostream>
using namespace std;
int main()
{
  // Implicit Type Conversion
  int intVar = 10;
  float floatVar = 5.5;
  double doubleVar;

  // Implicit conversion from int to double
  doubleVar = intVar;
  cout << "\nImplicit Conversion (int to double): " << doubleVar;

  // Implicit conversion from float to double
  doubleVar = floatVar;
  cout << "\nImplicit Conversion (float to double): " << doubleVar;

  // Explicit Type Conversion
  double anotherDoubleVar = 9.99;
  int anotherIntVar;

  // Explicit conversion from double to int
  anotherIntVar = static_cast<int>(anotherDoubleVar);
  cout << "\nExplicit Conversion (double to int): " << anotherIntVar;

  // Explicit conversion from float to int
  anotherIntVar = static_cast<int>(floatVar);
  cout << "\nExplicit Conversion (float to int): " << anotherIntVar;

  return 0;
}