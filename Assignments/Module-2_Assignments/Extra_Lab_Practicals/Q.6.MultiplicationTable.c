// Write a C program that takes an integer input from the user and prints its multiplication
// table using a for loop.
// Challenge: Allow the user to input the range of the multiplication table (e.g., from 1 to N).

#include <stdio.h>
int main()
{
  int number, range;

  // Taking input from the user
  printf("Enter an integer to print its multiplication table: ");
  scanf("%d", &number);
  printf("Enter the range up to which you want the multiplication table: ");
  scanf("%d", &range);

  // Print the multiplication table
  printf("Multiplication table of %d up to %d:\n", number, range);
  for (int i = 1; i <= range; i++)
  {
    printf("%d x %d = %d\n", number, i, number * i);
  }

  return 0;
}