#include<stdio.h>

int main()
{
    int a = 10, b;

    a++;     // valid (what is not valid a=a++)
    // b = ++a;
    // b++; // valid
    // b=--a; // valid first decrement then assign
    // b=a--; // valid first assign then decrement
    // b= a++ + ++a; // valid
    b = ++a+a++; // valid

    printf("%d\n", a);
    printf("%d\n", b);

    return 0;
}
