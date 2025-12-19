#include <stdio.h>

void swap(int a, int b)
{
  int c;
  c = a;
  a = b;
  b = c;
  printf("After swaping the values of a=%d and b=%d\n", a, b); // here the values are changed like swaped
}

int main()
{

  int a = 10, b = 20;
  swap(a, b);
  printf("the value of swaping in the main function: a=%d and b=%d\n", a, b); // these values are still the same which are declared
  return 0;
}