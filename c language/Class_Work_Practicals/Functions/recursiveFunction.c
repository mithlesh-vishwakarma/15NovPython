#include <stdio.h>
int factFind(int num)
{
  int f;
  if (num == 1)
  {
    return 1;
  }
  f = num * factFind(num - 1); // f = 5 * fact(4) * fact(3) * fact(2) * fact(1)
  return f;
}

int main()
{
  printf("the factorial is: %d", factFind(5));
  return 0;
}