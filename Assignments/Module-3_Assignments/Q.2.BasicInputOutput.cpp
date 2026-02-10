// 2. Basic Input/Output
// Write a C++ program that accepts user input for their name and age and then
// displays a personalized greeting.
// Objective: Practice input/output operations using cin and cout.

#include <iostream>
using namespace std;
int main()
{
  string name;
  int age;

  // Accept user input
  cout << "Enter your name: ";
  cin >> name;
  cout << "Enter your age: ";
  cin >> age;

  // Display personalized greeting
  cout << "\nHello, " << name << "! You are " << age << " years old.";

  return 0;
}