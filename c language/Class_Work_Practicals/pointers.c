#include <stdio.h>
int main()
{
  int a = 10;
  int *ptr;
  ptr = &a;

  printf("the Address: %c and the Value: %d", ptr, *ptr);
  *ptr = 100;
  printf("\n a=%d", a);
  return 0;
}