#include<stdio.h>
#include<math.h>
int main()
{
  int num, cube, square;
  printf("Enter an integer: \n");
  scanf("%d", &num);
  
  cube = pow(num, 3);
  square = pow(num, 2);
  
  printf("Cube of %d is %d\n", num, cube);
  printf("Square of %d is %d\n", num, square);
  
  return 0;
}