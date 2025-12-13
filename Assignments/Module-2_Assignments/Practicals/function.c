// Write a C program that calculates the factorial of a number using a function.Include function declaration, definition, and call.

#include <stdio.h>

int FactNum(int num); // declaration part of the code
int main()
{
  printf("%d", FactNum(5)); // calling the function
  return 0;
}

int FactNum(int num) // definition of the function
{
  int fact;
  if (num == 1)
  {
    return 1;
  }
  fact = num * FactNum(num - 1);
  return fact;
}