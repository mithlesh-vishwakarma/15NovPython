// Write a program to find the factorial of given number. 

#include<stdio.h>
int main(){

int i,n;
int fact=1;
printf("Please Enter The number\n");
scanf("\n%d",&n);

 for (i=0;i<n;i++){

  fact=fact*(n-i);


 }
printf("%d",fact);
return 0;
}