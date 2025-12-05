//Write a program to check temperature range (cold, warm, hot, very hot) using else-if
//ladder. 

// Below 10°C → Cold
// 10°C to 25°C → Warm
// 26°C to 35°C → Hot
// Above 35°C → Very Hot

#include<stdio.h>
int main(){
  int temperature;
  printf("enter the temperature in degree celsius: ");
  scanf("%d",&temperature);

  if(temperature<10){
    printf("the temperature is cold");
  }else if(temperature>=10 && temperature<=25){
    printf("the temperature is warm");
  }else if(temperature>=26 && temperature<=35){
    printf("the temperature is hot");
  }else if(temperature>35){
    printf("the temperature is very hot");
  }else{
    printf("please enter valid temperature");
  }
  return 0;
}