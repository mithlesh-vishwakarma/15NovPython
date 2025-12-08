// 28. Write a program to find the minimum digit of given number.HINT : (5167 = > 1 is min number)

#include <stdio.h>

int main()
{
  int num, min = 9, digit;
  // int min = 9; // start with the highest possible digit
  // int digit;
  printf("enter the number:\n");
  scanf("%d", &num);

  while (num > 0)
  {
    digit = num % 10; // get last digit
    printf("%d\t", digit);
    if (digit < min)
    {
      min = digit; // update minimum
      printf("%d\n", min);
    }

    num = num / 10; // remove last digit
  }

  printf("Minimum digit is: %d\n", min);
  return 0;
}
