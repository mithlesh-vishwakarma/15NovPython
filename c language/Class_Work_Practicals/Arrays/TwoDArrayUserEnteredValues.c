#include <stdio.h>
int main()
{
  int a[100][100], row, cols;
  printf("please enter the number of rows\n");
  scanf("%d", &row);
  printf("please enter the number of cols\n");
  scanf("%d", &cols);
  printf("please enter the elements of the array\n");

  for (int i = 0; i < row; i++)
  {
    for (int j = 0; j < cols; j++)
    {
      printf("\n Enter the a[%d][%d]", i, j);
      scanf("%d", &a[i][j]);
    }
  }
  for (int i = 0; i < row; i++)
  {
    for (int j = 0; j < cols; j++)
    {
      printf("\t%d", a[i][j]);
    }
    printf("\n");
  }

  return 0;
}