// Write a C program that takes an integer from the user and checks the following using
// different operators :
// Whether the number is even or odd.
// Whether the number is positive, negative, or zero.
// Whether the number is a multiple of both 3 and 5.

#include <stdio.h>
int main()
{
  int number;

  // Taking input from the user
  printf("Enter an integer: ");
  scanf("%d", &number);

  // Check if the number is even or odd
  if (number % 2 == 0)
    printf("%d is even.\n", number);
  else
    printf("%d is odd.\n", number);

  // Check if the number is positive, negative, or zero
  if (number > 0)
    printf("%d is positive.\n", number);
  else if (number < 0)
    printf("%d is negative.\n", number);
  else
    printf("The number is zero.\n");

  // Check if the number is a multiple of both 3 and 5
  if (number % 3 == 0 && number % 5 == 0)
    printf("%d is a multiple of both 3 and 5.\n", number);
  else
    printf("%d is not a multiple of both 3 and 5.\n", number);

  return 0;
}