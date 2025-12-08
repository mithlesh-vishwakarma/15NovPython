#include <stdio.h>
int main()
{

  for (int i = 1; i <= 5; i++)
  {

    for (int k = 1; k <= i; k++)
    {
      printf(" ");
    }
    for (int j = 9; j >= i; j--)
    {
      if (i == 1)
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