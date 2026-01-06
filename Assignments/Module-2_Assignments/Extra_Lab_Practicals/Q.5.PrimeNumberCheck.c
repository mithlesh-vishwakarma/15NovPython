// Write a C program that checks whether a given number is a prime number or not using a for
// loop.
// Challenge: Modify the program to print all prime numbers between 1 and a given number.

#include <stdio.h>
int main()
{
  int number, i, isPrime;

  // Taking input from the user
  printf("Enter a positive integer: ");
  scanf("%d", &number);

  printf("Prime numbers between 1 and %d are:\n", number);
  for (int num = 2; num <= number; num++)
  {
    isPrime = 1; // Assume the number is prime

    // Check if num is prime
    for (i = 2; i <= num / 2; i++)
    {
      if (num % i == 0)
      {
        isPrime = 0; // num is not prime
        break;
      }
    }

    if (isPrime)
    {
      printf("%d ", num);
    }
  }
  printf("\n");

  return 0;
}