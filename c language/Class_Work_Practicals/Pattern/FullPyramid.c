#include <stdio.h>
int main()
{

  int i, j, k;
  for (i = 1; i <= 5; i++)
  {
    for (k = 4; k >= i; k--) // k is for space printing, comparing with i(row number )
    {
      printf(" ");
    }
    for (j = 1; j <= i; j++) // j is for star printing, companing with i(row number )
    {
      // printf("*"); // Pattern left half pyramid
      printf("* "); // Pattern center aligned whole pyramid
    }
    printf("\n");
  }
}

/*
left half pyramid
----------------------

    *
   * *
  * * *
 * * * *
* * * * *



*/