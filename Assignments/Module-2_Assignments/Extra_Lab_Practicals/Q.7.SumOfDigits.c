// Write a C program that takes an integer from the user and calculates the sum of its digits
// using a while loop.
// Challenge : Extend the program to reverse the digits of the number.

#include <stdio.h>
int main()
{
  int number, sum = 0, reversedNumber = 0;

  // Taking input from the user
  printf("Enter an integer: ");
  scanf("%d", &number);

  // Calculate the sum of digits and reverse the number
  while (number != 0)
  {
    int digit = number % 10;                      // Get the last digit
    sum += digit;                                 // Add it to the sum
    reversedNumber = reversedNumber * 10 + digit; // Build the reversed number
    number /= 10;                                 // Remove the last digit
  }

  // Display the results
  printf("Sum of digits: %d\n", sum);
  printf("Reversed number: %d\n", reversedNumber);

  return 0;
}