#include <stdio.h>
int main()
{
  int a[10];
  for (int i = 0; i < 10; i++)
  {
    printf("please enter the value of a[%d]=", i);
    scanf("%d", &a[i]);
  }
  int even = 0, odd;
  for (int i = 0; i < 10; i++)
  {

    if (a[i] % 2 == 0)
    {
      printf("the value of evens a[%d]=%d\n", i, a[i]);
      even++;
    }
    else
    {
      printf("the values odds are a[%d]=%d\n", i, a[i]);
      odd++;
    }
  }
  printf("total even %d and total odd %d", even, odd);

  return 0;
}