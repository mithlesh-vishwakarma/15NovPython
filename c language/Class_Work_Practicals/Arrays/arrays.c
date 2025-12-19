#include <stdio.h>
int main()
{
  int a[5];
  // int a[5] = {23, 32, 34, 35, 43};
  // printf("the value of index is :%d", a[3]);
  for (int i = 0; i < 5; i++)
  {
    printf("please enter the value of a[%d]=", i);
    scanf("%d", &a[i]);
  }

  for (int i = 0; i < 5; i++)
  {
    printf("the value of a[%d]=%d\n", i, a[i]);
  }

  return 0;
}
