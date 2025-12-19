#include <stdio.h>

void swap(int *a, int *b)
{
  int c;
  c = *a;
  *a = *b;
  *b = c;
  // printf("After swaping the values of a=%p and b=%p\n", a, b);
}

int main()
{

  int a = 10, b = 20;
  swap(&a, &b);
  printf("the value of swaping in the main function: a=%d and b=%d\n", a, b); // these values are chnaged  swaped when call by it's address
  return 0;
}