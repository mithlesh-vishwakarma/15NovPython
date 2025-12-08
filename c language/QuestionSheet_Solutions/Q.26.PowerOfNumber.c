// 26. Write a program to find the power of a number using loop.

#include <stdio.h>
int main()
{
  int num, power;
  double Ans = 1;
  printf("enter the number:\n");
  scanf("%d", &num);
  printf("enter the power number:\n");
  scanf("%d", &power);
  while (power != 0)
  {
    Ans = Ans * num;
    power--;
  }
  printf("the Answer is: %f", Ans);
  return 0;
}