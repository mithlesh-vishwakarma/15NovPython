// Write a C program that generates Pascal’s Triangle up to N rows using loops.Implement the same program using a recursive function.

#include <stdio.h>

int factorial(int n)
{
  if (n == 0 || n == 1)
    return 1;
  return n * factorial(n - 1);
}
void print_pascals_triangle_recursive(int n, int row, int col)
{
  if (row == n)
    return;

  if (col > row)
  {
    printf("\n");
    print_pascals_triangle_recursive(n, row + 1, 0);
    return;
  }

  int coeff = factorial(row) / (factorial(col) * factorial(row - col));
  printf("%d ", coeff);

  print_pascals_triangle_recursive(n, row, col + 1);
}
int main()
{
  int n;

  printf("Enter the number of rows for Pascal's Triangle: ");
  scanf("%d", &n);

  printf("Pascal's Triangle (using loops):\n");
  for (int row = 0; row < n; row++)
  {
    for (int space = 0; space < n - row - 1; space++)
      printf(" ");

    for (int col = 0; col <= row; col++)
    {
      int coeff = factorial(row) / (factorial(col) * factorial(row - col));
      printf("%d ", coeff);
    }
    printf("\n");
  }

  printf("Pascal's Triangle (using recursion):\n");
  print_pascals_triangle_recursive(n, 0, 0);

  return 0;
}