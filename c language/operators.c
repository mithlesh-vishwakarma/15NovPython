#include<stdio.h>
int main()
{
  int a,b;
  printf( "enter values of a and b \n");
  scanf("%d %d",&a,&b);
  // sum=a+b;
  printf("\nsum=%d", a+b);
  printf("\nsub=%d", a-b);
  printf("\nmul=%d", a*b);
  printf("\ndiv=%f", (float)a/b);
  printf("\nmodulo=%d", a%b);

}