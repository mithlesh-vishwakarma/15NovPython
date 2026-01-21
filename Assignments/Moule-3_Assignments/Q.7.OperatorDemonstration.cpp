// 3. Operator Demonstration
// Write a C++ program that demonstrates arithmetic, relational, logical, and bitwise operators.Perform operations using each type of operator and display the results.
// Objective : Reinforce understanding of different types of operators in C++.

#include <iostream>
using namespace std;
int main()
{
  int a = 10, b = 5;

  // Arithmetic Operators
  cout << "Arithmetic Operators:";
  cout << "\ta + b = " << a + b;
  cout << "\ta - b = " << a - b;
  cout << "\ta * b = " << a * b;
  cout << "\ta / b = " << a / b;
  cout << "\ta % b = " << a % b;

  // Relational Operators
  cout << "\nRelational Operators:";
  cout << "\ta == b: " << (a == b);
  cout << "\ta != b: " << (a != b);
  cout << "\ta > b: " << (a > b);
  cout << "\ta < b: " << (a < b);
  cout << "\ta >= b: " << (a >= b);
  cout << "\ta <= b: " << (a <= b);

  // Logical Operators
  cout << "\nLogical Operators:";
  cout << "\t(a > b) && (a < 20): " << ((a > b) && (a < 20));
  cout << "\t(a < b) || (a < 20): " << ((a < b) || (a < 20));
  cout << "\t!(a > b): " << (!(a > b));

  // Bitwise Operators
  cout << "\nBitwise Operators:";
  cout << "\ta & b = " << (a & b);
  cout << "\ta | b = " << (a | b);
  cout << "\ta ^ b = " << (a ^ b);
  cout << "\t~a = " << (~a);
  cout << "\ta << 1 = " << (a << 1);
  cout << "\ta >> 1 = " << (a >> 1);

  return 0;
}