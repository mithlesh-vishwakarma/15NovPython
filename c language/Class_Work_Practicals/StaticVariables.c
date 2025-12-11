#include <stdio.h>

void incre()
{
  int a = 0;        // this will terminated all time like every time it's called by the main function.
  static int s = 0; // this remain the same during the whole programm doesn't terminated.
  a++;
  s++;
  printf("\n a=%d \t s=%d", a, s);
}

int main()
{

  for (int i = 0; i <= 4; i++)
  {
    incre();
  }
}
