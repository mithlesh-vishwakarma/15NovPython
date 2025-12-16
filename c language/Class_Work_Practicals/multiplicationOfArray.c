#include <stdio.h>
int main()
{
  int a[2][2], b[2][2], c[2][2];
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      printf("Enter the value of a[%d][%d]\n", i, j);
      scanf("%d", &a[i][j]);
    }
  }
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      printf("Enter the value of b[%d][%d]\n", i, j);
      scanf("%d", &b[i][j]);
    }
  }

  // multiplication of 2d array:

  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      c[i][j] = a[j][i] * b[i][j];
    }
    printf("\n");
  }
  printf("the value of a matrix:\n");
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      printf("%d\t", a[i][j]);
    }
    printf("\n");
  }
  printf("the value of b matrix:\n");
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      printf("%d\t", b[i][j]);
    }
    printf("\n");
  }
  printf("the value of sum a+b= c matrix:\n");
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      printf("\t%d", c[i][j]);
    }
    printf("\n");
  }

  return 0;
}