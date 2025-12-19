#include <stdio.h>
float pi = 3.14; // globle variable: we can access it anywhere in this programm

void testFunction()
{
  printf("\n in function pi=%f", pi);
}

void sum(int a, int b) // the formal parameter variable example: only accesible in the function
{
  printf("the sum in Function is:%d +%d = %d", a, b, a + b);
}

int main()
{
  {
    // local variable example : onoly accessible in the local block of code
    int x = 10;
    printf("the local variable value: x= %d", x);
  }

  testFunction();
  printf("\n the value of Pi=%f", pi);
}