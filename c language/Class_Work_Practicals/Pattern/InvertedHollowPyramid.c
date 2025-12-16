#include <stdio.h>
int main()
{
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
      //   printf("*");
      // }
    }
    for (int j = 6; j >= i; j--)
    {
      if (i == 1 || j == i || j == 6)
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

/*output

* * * * * *
 *       *
  *     *
   *   *
    * *
     *

*/