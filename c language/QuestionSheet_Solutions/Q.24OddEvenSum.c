// Write a program to find sum of all even and odd numbers separately from 1 to 10
#include <stdio.h>
int main()
{
  int num, sum = 0;
  printf("Enter The Number:\n");
  scanf("%d", &num);

  for (int i = 1; i <= num; i++)
  {
    printf("%d\n", i);

    if (i % 2 == 0)
    {

      sum = sum + i;
      printf("The Even Numbers are: %d\n", sum);
    }
    else
    {
      sum = sum + i;
      printf("The Odd Numbers are: %d\n", sum);
    }
  }

  return 0;
}