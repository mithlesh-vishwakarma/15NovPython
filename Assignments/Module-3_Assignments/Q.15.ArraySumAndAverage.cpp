// Array Sum and Average:
// Write a C++ program that accepts an array of integers, calculates the sum and average, and displays the results.
// Objective : Understand basic array manipulation.

#include <iostream>
using namespace std;
int main()
{
  int size;
  cout << "Enter the size of the array: ";
  cin >> size;

  int arr[size];

  cout << "Enter " << size << " integers:";
  for (int i = 0; i < size; i++)
  {
    cin >> arr[i];
  }

  int sum = 0;

  for (int i = 0; i < size; i++)
  {
    sum += arr[i];
  }

  double average = static_cast<double>(sum) / size;

  cout << "Sum: " << sum;
  cout << "Average: " << average;

  return 0;
}