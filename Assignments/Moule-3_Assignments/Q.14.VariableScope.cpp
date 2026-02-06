// Variable Scope : Write a program that demonstrates the difference between local and global variables in C++.Use functions to show scope.
// Objective : Reinforce the concept of variable scope.

#include <iostream>
using namespace std;

int globalVar = 10;

void demonstrateLocalScope()
{
  int localVar = 20;
  cout << "Inside demonstrateLocalScope function:";
  cout << "Local Variable: " << localVar;
  cout << "Global Variable: " << globalVar;
}
// Function to demonstrate variable shadowing
void demonstrateShadowing()
{
  int globalVar = 30; // Local variable with the same name as global variable
  cout << "Inside demonstrateShadowing function:";
  cout << "Local Variable (shadowing global): " << globalVar; // Accessing local variable
  cout << "Global Variable: " << ::globalVar;                 // Accessing global variable using scope resolution operator
}
int main()
{
  cout << "In main function:";
  cout << "Global Variable: " << globalVar; // Accessing global variable
  demonstrateLocalScope();                  // Call function to demonstrate local scope
  demonstrateShadowing();                   // Call function to demonstrate variable shadowing
  return 0;
}