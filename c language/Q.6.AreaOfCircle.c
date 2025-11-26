#include<stdio.h>
#include<math.h>
int main()
{
float AreaOfCircle;
float radius, pi = 3.14;
printf("Enter radius of circle: \n");
scanf("%f", &radius);

AreaOfCircle = pi * pow(radius, 2);

printf("Area of Circle is:%f\n", AreaOfCircle);  
return 0;

}