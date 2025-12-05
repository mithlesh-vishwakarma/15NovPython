// write a program to check whether the number is zero or non-zero.

#include<stdio.h>
int main(){
int number;

printf("enter a number:");
scanf("%d",&number);

if(number==0)
{
  printf("the number is zero");
}else{
  printf("the number is non-zero");
}
return 0;
}
