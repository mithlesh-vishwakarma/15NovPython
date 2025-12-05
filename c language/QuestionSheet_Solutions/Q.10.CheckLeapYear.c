// write a programm to check whether a year is leap year or not.
#include<stdio.h>
int main(){
  int year;
  printf("enter a year: ");
  scanf("%d",&year);

  if((year %4==0 && year %100!=0) || (year %400==0)){
    printf("the year is leap year");
  }else{
    printf("the year is not leap year");
  }
  return 0;
}