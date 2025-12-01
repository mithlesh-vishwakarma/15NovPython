// Write a program to check whether a number is divisible by both 3 and 5 using nested if

#include<stdio.h>
int main(){
int number;
printf("enter a number :\n");
scanf("%d",&number);

if(number%3==0){
  if(number%5==0){

    printf("the number is divisible by 3 and 5");
  }else{
    printf("the number is not divisible by 3 and 5 ");
  }
}else{
  printf("the number is not divisible by 3 and 5");
}
return 0;
}