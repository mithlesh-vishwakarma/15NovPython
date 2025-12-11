#include <stdio.h>
int revNumFind(int num)
{
  // int rev = 0;
  int rem;
  static int rev = 0;
  if (num == 0)
  {
    return 0;
  }
  rem = num % 10;
  rev = rev * 10 + rem;
  printf("\n the rev is%d", rev);
  revNumFind(num / 10);
  return rev;
}

int main()
{

  printf("reverse num:%d", revNumFind(1234));
}