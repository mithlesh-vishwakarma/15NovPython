#include <stdio.h>
int main()
{
  int a[5];
  for (int i = 0; i < 5; i++)
  {
    printf("please enter the value of a[%d]=", i);
    scanf("%d", &a[i]);
  }

  int temp;
  for (int i = 0; i < 5; i++)
  {
    for (int j = i + 1; j < 5; j++)
    {
      // if (a[i] > a[j])   // for accending orders
      if (a[i] < a[j]) // for deccending orders
      {
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;
      }
    }
  }
  printf("the value of sorting arrays are\n");
  for (int i = 0; i < 5; i++)
  {
    printf("%d\t", a[i]);
  }
  return 0;
}