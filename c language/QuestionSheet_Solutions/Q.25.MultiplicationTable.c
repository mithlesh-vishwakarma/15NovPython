// 25. Write a program to display the multiplication table of given number.
#include <stdio.h>
int main()
{
  int num;
  printf("please enter the number\n");
  scanf("%d", &num);
  printf("the table of %d is: \n", num);
  for (int i = 1; i <= 10; i++)
  {

    printf("%d x %d = %d\n", num, i, num * i);
  }
  return 0;
}