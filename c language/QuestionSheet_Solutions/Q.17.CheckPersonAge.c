/*Write a program to classify a person based on age (child, teenager, adult, senior)
using else-if. */

//0 to 12 → Child
//13 to 19 → Teenager
//20 to 59 → Adult
//60 and above → Senior

#include<stdio.h>
int main(){
int age;

printf("enter the age of person:");
scanf("%d",&age);
if(age>=0 && age<=12){
  printf("the person is child");
}else if(age>=13 && age<=19){
  printf("the person is teenager");
}else if(age>=20 && age<=59){
  printf("the person is adult");
}else if(age>=60){
  printf("the person is senior");
}else{
  printf("please enter valid age"); 
}
return 0;

}