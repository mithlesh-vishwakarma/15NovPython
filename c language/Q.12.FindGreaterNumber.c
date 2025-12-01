// write a prigramm to find a greater of two numbers

#include<stdio.h>
int main(){
int num1,num2;

printf("enter the num1 and num2:");
scanf("%d %d",&num1,&num2);

if(num1>num2)
{
  printf("the %d is greater than %d",num1,num2);
}else{
  printf("%d is greater than %d",num2,num1);
}

}