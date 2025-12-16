// 27. Write a program to find the sum of first and last digit of number.HINT : (number = 4216 = > 4 + 6 = 10)

#include <stdio.h>
int main()
{
  int num = 0;
  printf("enter the number:\n");
  scanf("%d", &num);
  int last = num % 10;
  while (num > 9) // because of the single digit number
  {
    num = num / 10; // to get single digit number :until it get the first single digit
    // printf("%d\n", num);
  }
  printf("the sum is:%d", last + num);
  return 0;
}