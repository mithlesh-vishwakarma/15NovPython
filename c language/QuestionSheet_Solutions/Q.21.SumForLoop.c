// Write a program to print the sum of first 20 numbers using for loop.

#include<stdio.h>
int main()
{
int sum=0;

for(int i=1;i<=20;i++){
printf("\n%d",i);
sum=sum+i;
printf ("%d",i); // output are double printing. why??
}

printf("\n sum of first 20 numbers is %d",sum);
return 0;

}


/*

*** output***
11
22
33
44
55
66
77
88
99
1010
1111
1212
1313
1414
1515
1616
1717
1818
1919
2020
 sum of first 20 numbers is 210

*/