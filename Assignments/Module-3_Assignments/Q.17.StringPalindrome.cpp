// String Palindrome Check:
// Write a C++ program to check if a given string is a palindrome(reads the same forwards and backwards).
// Objective : Practice string operations.

#include <iostream>
#include <string>
using namespace std;
int main()
{
  string str;
  cout << "Enter a string: ";
  getline(cin, str);

  string reversedStr = "";
  for (int i = str.length() - 1; i >= 0; i--)
  {
    reversedStr += str[i];
  }

  if (str == reversedStr)
  {
    cout << "The string is a palindrome.";
  }
  else
  {
    cout << "The string is not a palindrome.";
  }

  return 0;
}