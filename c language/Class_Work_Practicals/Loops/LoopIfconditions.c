#include<stdio.h>
int main() {
    int i,sum=0;
    for(i = 3; i <= 10; i++) {
        printf("I= %d\n", i);
        if (i%2==0)
        {
         sum=sum+i;
        }
    }
    printf("Sum= %d\n",sum);
    return 0;
}


