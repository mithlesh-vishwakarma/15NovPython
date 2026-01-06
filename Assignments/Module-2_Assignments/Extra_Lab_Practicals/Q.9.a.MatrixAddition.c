// Write a C program that accepts two 2x2 matrices from the user and adds them.Display the resultant matrix.
// Challenge : Extend the program to work with 3x3 matrices and matrix multiplication.

#include <stdio.h>
int main()
{
  int matrix1[2][2], matrix2[2][2], sum[2][2];

  // Taking input for the first matrix
  printf("Enter elements of the first 2x2 matrix:\n");
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      printf("Element [%d][%d]: ", i + 1, j + 1);
      scanf("%d", &matrix1[i][j]);
    }
  }

  // Taking input for the second matrix
  printf("Enter elements of the second 2x2 matrix:\n");
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      printf("Element [%d][%d]: ", i + 1, j + 1);
      scanf("%d", &matrix2[i][j]);
    }
  }

  // Adding the two matrices
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      sum[i][j] = matrix1[i][j] + matrix2[i][j];
    }
  }

  // Displaying the resultant matrix
  printf("Resultant matrix after addition:\n");
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      printf("%d ", sum[i][j]);
    }
    printf("\n");
  }

  return 0;
}