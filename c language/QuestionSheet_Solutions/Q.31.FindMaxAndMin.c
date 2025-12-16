// 31. Write a program to find min and max elements from a given array.

#include <stdio.h>
int main()
{
  int a[100], size;
  printf("enter the size of the array\n");
  scanf("%d", &size);
  printf("enter the Elements of the array\n");
  for (int i = 0; i < size; i++)
  {
    scanf("%d", &a[i]);
  }
  int max = a[0];
  int min = a[0];

  for (int i = 0; i < size; i++)
  {
    if (a[i] > max)
    {
      max = a[i];
    }
    else if (a[i] < min)
    {
      min = a[i];
    }
  }

  printf("the min value is %d\n", min);
  printf("the max value is %d\n", max);

  return 0;
}