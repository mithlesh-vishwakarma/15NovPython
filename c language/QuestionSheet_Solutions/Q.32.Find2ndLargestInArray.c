// 32. Write a program to find second largest number from a given array.

#include <stdio.h>
int main()
{
  int a[5];
  for (int i = 0; i < 5; i++)
  {
    printf("Enter the a[%d]=", i);
    scanf("%d", &a[i]);
  }

  int max1, max2;
  if (a[0] > a[1])
  {
    max1 = a[0];
    max2 = a[1];
  }
  else
  {
    max2 = a[0];
    max1 = a[1];
  }
  for (int i = 2; i < 5; i++)
  {
    if (a[i] > max1)
    {
      max2 = max1;
      max1 = a[i];
    }
    else if (a[i] > max2)
    {
      max2 = a[i];
    }
  }
  printf("the second largest number is %d", max2);

  return 0;
}