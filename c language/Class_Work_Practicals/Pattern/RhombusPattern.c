#include <stdio.h>
int main()
{

  for (int i = 1; i <= 6; i++)
  {

    for (int k = 1; k <= i; k++)
    {
      if (k == i)
      {
        printf(" ");
      }
    }

    for (int j = 1; j <= 6 + i; j++)
    {
      printf("*");
    }
    printf("\n");
  }

  return 0;
}