// reverse any numbers any degits 

#include<stdio.h>
int main(){

int num, rev=0, rem;
printf("Enter any number: ");
scanf("%d",&num);
while(num!=0){
    rem = num % 10;
    printf("\n rem=%d",rem);
    num = num / 10;
    printf("\n num is: %d",num);
    rev = rev * 10 + rem;
    printf("\t Reverse number is: %d",rev);
    
}
return 0;
}