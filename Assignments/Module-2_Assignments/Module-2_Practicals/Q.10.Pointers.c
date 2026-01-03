// Write a C program to demonstrate pointer usage.Use a pointer to modify the value of a variable and print the result.

#include <stdio.h>
int main()
{
  int var = 10;
  int *ptr;   // pointer declaration
  ptr = &var; // pointer initialization

  printf("Value of var before modification: %d\n", var);

  // Modifying the value of variable using pointer
  *ptr = 20;

  printf("Value of var after modification using pointer: %d\n", var);

  return 0;
}