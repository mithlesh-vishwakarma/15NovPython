#include <stdio.h>
int main()
{
  for (int i = 1; i <= 6; i++)
  {
    for (int k = 6; k >= i; k--)
    {
      if (k != i)
      {
        printf(" ");
      }
      // else
      // {
      //   printf("* ");
      // }
    }
    for (int j = 1; j <= i; j++)
    {
      if (j == i || j == 1)
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
  for (int i = 1; i <= 6; i++)
  {
    for (int k = 1; k <= i; k++)
    {
      if (k != i)
      {
        printf(" ");
      }
      // else
      // {
      //   printf("* ");
      // }
    }
    for (int j = 6; j >= i; j--)
    {
      if (j == i || j == 6)
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

/*
output

     *
    * *
   *   *
  *     *
 *       *
*         *
*         *
 *       *
  *     *
   *   *
    * *
     *

*/