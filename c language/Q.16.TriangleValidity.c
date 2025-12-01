/*Write a program to check if a triangle is valid and also equilateral, isosceles or
scalene using nested if.*/ 
#include<stdio.h>
int main(){
int a,b,c;
printf("enter the three sides of triangle:\n");
scanf("%d %d %d",&a,&b,&c);

if(a+b>c && b+c>a && c+a>b){
  printf("the triangle is valid\n"); // check the validity of triangle
  if(a==b && b==c){
    printf("the triangle is equilateral");  // if two side are same then it is quilaterial
  }else if(a==b || b==c || c==a){
    printf("the triangle is isosceles"); // if all side are same then it is isosceles
  }else{
    printf("the triangle is scalene");  // if no side are same then it is scalene
   }
}
return 0;
}