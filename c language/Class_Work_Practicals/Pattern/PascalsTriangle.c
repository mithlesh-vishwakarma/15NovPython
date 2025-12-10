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
