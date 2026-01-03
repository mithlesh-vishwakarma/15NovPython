// Write a C program that accepts two integers from the user and performs
// arithmetic, relational, and logical operations on them.Display the results.

#include <stdio.h>
int main()
{
  int a, b;
  printf("enter values of a and b \n");
  scanf("%d %d", &a, &b);
  // sum=a+b;
  printf("\nsum=%d", a + b);
  printf("\nsub=%d", a - b);
  printf("\nmul=%d", a * b);
  printf("\ndiv=%f", (float)a / b);
  printf("\nmodulo=%d", a % b);
  return 0;
}

/*
output:
-------
enter values of a and b
34
43

sum=77
sub=-9
mul=1462
div=0.790698
modulo=34

*/