// Write a C program that accepts two 3x3 matrices from the user and adds them and do multiplication. Display the resultant matrix.

#include <stdio.h>
int main()
{
  int matrix1[3][3], matrix2[3][3], sum[3][3], product[3][3];

  // Taking input for the first matrix
  printf("Enter elements of the first 3x3 matrix:\n");
  for (int i = 0; i < 3; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      printf("Element [%d][%d]: ", i + 1, j + 1);
      scanf("%d", &matrix1[i][j]);
    }
  }

  // Taking input for the second matrix
  printf("Enter elements of the second 3x3 matrix:\n");
  for (int i = 0; i < 3; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      printf("Element [%d][%d]: ", i + 1, j + 1);
      scanf("%d", &matrix2[i][j]);
    }
  }

  // Adding the two matrices
  for (int i = 0; i < 3; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      sum[i][j] = matrix1[i][j] + matrix2[i][j];
    }
  }

  // Multiplying the two matrices
  for (int i = 0; i < 3; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      product[i][j] = 0;
      for (int k = 0; k < 3; k++)
      {
        product[i][j] += matrix1[i][k] * matrix2[k][j];
      }
    }
  }

  // Displaying the resultant matrix after addition
  printf("Resultant matrix after addition:\n");
  for (int i = 0; i < 3; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      printf("%d ", sum[i][j]);
    }
    printf("\n");
  }

  // Displaying the resultant matrix after multiplication
  printf("Resultant matrix after multiplication:\n");
  for (int i = 0; i < 3; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      printf("%d ", product[i][j]);
    }
    printf("\n");
  }

  return 0;
}