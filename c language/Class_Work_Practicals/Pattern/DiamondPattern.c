#include <stdio.h>
int main()
{
  for (int i = 0; i <= 6; i++)
  {
    for (int k = 6; k >= i; k--)
    {
      printf(" ");
    }
    for (int j = 1; j <= i; j++)
    {

      printf("* ");
    }
    printf("\n");
  }
  for (int i = 0; i <= 6; i++)
  {
    for (int k = 1; k <= i; k++)
    {
      printf(" ");
    }
    for (int j = 6; j >= i; j--)
    {

      printf("* ");
    }
    printf("\n");
  }

  return 0;
}

/*diamond pattern
output:
-----------


      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *
* * * * * * *
 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *


*/