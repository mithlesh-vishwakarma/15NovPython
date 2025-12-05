// write a program to check whether a person is eligible to vote or not. (age limit is 18 years)

#include<stdio.h>
int main(){

int age;

printf (" enter your age: ");
scanf("%d",&age);

if(age>=18){
  printf("you ar eligible for vote");
}else{  
  printf("you are not eligible for vote");  

}
return 0;
}