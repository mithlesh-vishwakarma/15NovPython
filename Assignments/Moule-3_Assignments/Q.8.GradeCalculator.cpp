// 1. Grade Calculator
// Write a C++ program that takes a student’s marks as input and calculates the grade based on if - else conditions.
// Objective : Practice conditional statements(if - else).

#include <iostream>
using namespace std;
int main()
{
  int marks;
  char grade;

  // Accept user input
  cout << "Enter the student's marks (0-100): ";
  cin >> marks;

  // Calculate grade based on marks
  if (marks >= 90 && marks <= 100)
  {
    grade = 'A';
  }
  else if (marks >= 80 && marks < 90)
  {
    grade = 'B';
  }
  else if (marks >= 70 && marks < 80)
  {
    grade = 'C';
  }
  else if (marks >= 60 && marks < 70)
  {
    grade = 'D';
  }
  else if (marks >= 0 && marks < 60)
  {
    grade = 'F';
  }
  else
  {
    cout << "Invalid marks entered. Please enter marks between 0 and 100." << endl;
    return 1; // Exit with error code
  }

  // Display the result
  cout << "\nThe grade for marks " << marks << " is: " << grade << endl;

  return 0;
}