// Write a program to find sum of all even and odd numbers separately from 1 to 10
#include <stdio.h>
int main()
{
  int num, EvenSum = 0, OddSum = 0;
  printf("Enter The Number:\n");
  scanf("%d", &num);

  // printf("The Even Numbers between 1 to %d:\n", num);
  for (int i = 1; i <= num; i++)
  {
    // printf("%d\n", i);

    if (i % 2 == 0)
    {
      // printf("%d\n", i);
      EvenSum = EvenSum + i;
    }

    if (i % 2 != 0)
    {
      // printf("%d\n", i);
      OddSum = OddSum + i;
    }
    }
  printf("The Sum of Even Numbers is %d\n", EvenSum);
  // printf("The Odd Numbers between 1 to %d:\n", num);
  printf("The Sum of Even Numbers is %d\n", OddSum);

  return 0;
}