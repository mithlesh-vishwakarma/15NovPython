#include <stdio.h>

int main()
{
  int row1, col1, row2, col2;
  int i, j, k;

  // Input sizes
  printf("Enter rows and columns for matrix A: ");
  scanf("%d %d", &row1, &col1);

  printf("Enter rows and columns for matrix B: ");
  scanf("%d %d", &row2, &col2);

  // Check multiplication condition
  if (col1 != row2)
  {
    printf("Matrix multiplication not possible.\n");
    return 0;
  }

  // Declare matrices
  int a[row1][col1];
  int b[row2][col2];
  int c[row1][col2];

  // Input matrix A
  printf("Enter elements of matrix A:\n");
  for (i = 0; i < row1; i++)
  {
    for (j = 0; j < col1; j++)
    {
      scanf("%d", &a[i][j]);
    }
  }

  // Input matrix B
  printf("Enter elements of matrix B:\n");
  for (i = 0; i < row2; i++)
  {
    for (j = 0; j < col2; j++)
    {
      scanf("%d", &b[i][j]);
    }
  }

  // Matrix multiplication
  for (i = 0; i < row1; i++)
  {
    for (j = 0; j < col2; j++)
    {
      c[i][j] = 0;
      for (k = 0; k < col1; k++)
      {
        c[i][j] += a[i][k] * b[k][j];
      }
    }
  }

  // Print matrix A
  printf("\nMatrix A:\n");
  for (i = 0; i < row1; i++)
  {
    for (j = 0; j < col1; j++)
    {
      printf("%d\t", a[i][j]);
    }
    printf("\n");
  }

  // Print matrix B
  printf("\nMatrix B:\n");
  for (i = 0; i < row2; i++)
  {
    for (j = 0; j < col2; j++)
    {
      printf("%d\t", b[i][j]);
    }
    printf("\n");
  }

  // Print result matrix C
  printf("\nMatrix C (A × B):\n");
  for (i = 0; i < row1; i++)
  {
    for (j = 0; j < col2; j++)
    {
      printf("%d\t", c[i][j]);
    }
    printf("\n");
  }

  return 0;
}
