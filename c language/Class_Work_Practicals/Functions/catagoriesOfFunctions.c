#include <stdio.h>

// without return type without parameter
void display()
{
  printf("Hello mithlesh..!!!");
}
// without return type with parameter
void areaOfRect(int l, int b)
{
  printf("area =%d", l * b);
}
// with return type without parameter

int square()
{
  int num;
  printf("please enter the value:");
  scanf("%d", &num);
  int s = num * num;
  return s;
}

// with return type with parameter
int add(int a, int b)
{
  int c = a + b;
  return c;
}

int main()
{
  display();
  areaOfRect(3, 4);
  printf("the sum is: %d\n", add(100, 200));
  printf("the square is: %d\n", square());

  return 0;
}