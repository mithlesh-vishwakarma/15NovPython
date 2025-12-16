// 29. Write a program to find sum of all even elements of a given array.

#include <stdio.h>
int main()
{
  int arr[10];

  for (int i = 0; i < 10; i++)
  {
    printf("please enter a[%d]=", i);
    scanf("%d", &arr[i]);
  }

  int even = 0;
  for (int i = 0; i < 10; i++)
  {
    if (arr[i] % 2 == 0)
    {
      printf("the Evens Are arr[%d]= %d\n", i, arr[i]);
      even = even + arr[i];
    }

    printf("the Sum of Evens Are %d\n", even);

    return 0;
  }
}