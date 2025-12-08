#include <stdio.h>
int main()
{

  for (int i = 1; i <= 10; i++)
  {

    for (int k = 1; k <= i; k++)
    {
      if (k == i)
      {
        printf("*");
      }
      printf(" ");
    }
    for (int j = 10; j >= i; j--)
    {
      if (i == 1 || j == i || i == j)
      {
        printf("* ");
      }
      else
      {
        printf("  ");
      }
    }

    printf("\n");
  }

  return 0;
}