#include <stdio.h>
int main()
{
  printf("please enter the values");
  int a[2][2];

  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j)
    {
      printf("enter the elements for all \n");
      scanf("%d", &a[i][j]);
    }
  }

  return 0;
}