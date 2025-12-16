// 30. Write a program to create a new array of only odd numbers from a given array elements.
#include <stdio.h>
int main()
{
  int a[10];
  printf("please enter the 10 numbers of array");

  for (int i = 0; i < 10; i++)
  {
    scanf("%d", &a[i]);
  }
  printf("the New crated array of odd numbers are\n");
  for (int i = 0; i < 10; i++)
  {
    if (a[i] % 2 != 0)
    {
      printf("%d\t", a[i]);
    }
  };
  return 0;
}