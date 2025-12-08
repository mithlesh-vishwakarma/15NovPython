// 23. Write a program to find the sum of digits of a number.
// hint 1234= 1+2+3+4

#include <stdio.h>
int main()
{

  int num, sum = 0, rem;
  printf("please enter the num: \n");
  scanf("%d", &num);

  while (num != 0)
  {
    rem = num % 10;
    // printf("the reminder is: %d\n", rem);
    num = num / 10;
    // printf("the number is: %d\t", num);
    sum = sum + rem;
    // printf("the sum of digit is: %d\n", sum);
  }
  printf("%d\n", sum);

  return 0;
}