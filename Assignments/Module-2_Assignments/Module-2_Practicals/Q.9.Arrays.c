// Write a C program that stores 5 integers in a one - dimensional array and prints them.Extend this to handle a two - dimensional array(3x3 matrix) and calculate the sum of all elements.
#include <stdio.h>
int main()
{
  int oneDArray[5];
  printf("Enter 5 integers for one-dimensional array:\n");
  for (int i = 0; i < 5; i++)
  {
    scanf("%d", &oneDArray[i]);
  }

  printf("You entered the following integers in the one-dimensional array:\n");
  for (int i = 0; i < 5; i++)
  {
    printf("%d ", oneDArray[i]);
  }
  printf("\n");

  int twoDArray[3][3];
  int sum = 0;
  printf("Enter elements for a 3x3 matrix:\n");
  for (int i = 0; i < 3; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      scanf("%d", &twoDArray[i][j]);
      sum += twoDArray[i][j];
    }
  }

  printf("The sum of all elements in the 3x3 matrix is: %d\n", sum);

  return 0;
}