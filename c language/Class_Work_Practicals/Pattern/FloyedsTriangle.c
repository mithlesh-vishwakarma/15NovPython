#include <stdio.h>
int main()
{
  int num = 1;
  for (int i = 1; i <= 4; i++)
  {
    // for (int k = 4; k >= i; k--)
    // {
    //   printf(" ");
    // }
    // printf("%d", i);
    for (int j = 1; j <= i; j++)
    {
      printf("%d", num);
      num++;
    }
    printf("");
  }
  return 0;
}

/*output
-----------
1
23
456
78910

*/