#include <stdio.h>
int main()
{
  int num, min = 9, digit;
  printf("please enter the number\n");
  scanf("%d", &num);

  while (num > 0)
  {
    digit = num % 10;
    printf("%d\t", digit);

    if (digit < min)
    {
      min = digit;
      printf("%d\t", min);
    }
    num = num / 10;
  }
  printf("the min is %d\n", min);
  return 0;
}