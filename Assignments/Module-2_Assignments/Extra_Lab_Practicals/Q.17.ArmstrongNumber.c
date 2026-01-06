// Write a C program that checks whether a given number is an Armstrong number or not(e.g.,
// 153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3)
//  Write a program to find all Armstrong numbers between 1 and 1000.

#include <stdio.h>
#include <math.h>
int is_armstrong(int num)
{
  int original = num;
  int sum = 0;
  int digits = 0;

  while (num != 0)
  {
    digits++;
    num /= 10;
  }

  num = original;

  while (num != 0)
  {
    int digit = num % 10;
    sum += pow(digit, digits);
    num /= 10;
  }

  return sum == original;
}
int main()
{
  int number;

  printf("Enter a number to check if it is an Armstrong number: ");
  scanf("%d", &number);

  if (is_armstrong(number))
  {
    printf("%d is an Armstrong number.\n", number);
  }
  else
  {
    printf("%d is not an Armstrong number.\n", number);
  }

  printf("Armstrong numbers between 1 and 1000 are:\n");
  for (int i = 1; i <= 1000; i++)
  {
    if (is_armstrong(i))
    {
      printf("%d ", i);
    }
  }
  printf("\n");

  return 0;
}