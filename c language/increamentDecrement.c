#include<stdio.h>

int main()
{
    int a = 10, b;

    a++;     // valid (what is not valid a=a++)
    // b = ++a;
    // b++; // valid
    // b=--a; // valid
    // b=a--; // valid
    b = ++a+a++; // valid

    printf("%d\n", a);
    printf("%d\n", b);

    return 0;
}
