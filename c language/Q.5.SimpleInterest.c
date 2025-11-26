#include<stdio.h>
#include<math.h>
int main()
{
  int simple_interest,principal,rate,time;
  printf("Enter principal amount, rate of interest and time(in years): \n");
  scanf("%d %d %d", &principal, &rate, &time);

  simple_interest = (principal * rate * time) / 100;

  printf("Simple Interest is: %d\n", simple_interest);

  
  return 0;
} 