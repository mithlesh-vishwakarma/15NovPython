#include <stdio.h>

int main()
{
  int ans;

  for (int i = 0; i <= 6; i++)
  {
    for (int k = 6; k >= i; k--)
    {
      printf(" ");
    }
    ans = 1;
    // Print values
    for (int j = 0; j <= i; j++)
    {
      printf(" %d", ans);
      ans = ans * (i - j) / (j + 1); // Pascal formula
    }

    printf("\n");
  }

  return 0;
}

/*

output

        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
   1 5 10 10 5 1
  1 6 15 20 15 6 1

*/