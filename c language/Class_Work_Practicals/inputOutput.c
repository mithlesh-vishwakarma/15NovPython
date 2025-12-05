#include<stdio.h>

int main()
{
    int number;
    char ch;
    float number2;
    
    printf("Please enter a character to print\n");
    scanf(" %c", &ch);            //problem found in runtime
    printf("character = %c\n", ch);

    printf("Please enter a number to print\n");
    scanf("%d", &number);
    printf("number = %d\n", number);


    printf("Please enter a float value to print\n");
    scanf("%f", &number2);      // now in float it is not asking value direct printing 0.000
    printf("number2 = %f\n", number2);

    return 0;
}
