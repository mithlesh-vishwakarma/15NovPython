#include <stdio.h>
void display();            // declaration of the functions
int add(int a, int b);     // declaration of the functions
float areaOfCircle(int r); // declaration of the function
int main()
{
  display();               // calling the function
  int sum = add(100, 200); // calling the function
  printf("the sum is: %d", sum);

  float area = areaOfCircle(4); // calling the function
  printf("\nthe area of circle = %.2f", area);
  return 0;
}

void display() // defination of function
{
  printf("Hello world\n");
}

int add(int a, int b) // defination of the function
{
  int c = a + b;
  return c;
}
float areaOfCircle(int r)
{
  float area = 3.14 * (float)r * (float)r;
  return area;
}