#include<stdio.h>
int main()
{
int num1,num2, sum,sub,mul,mod;
float div;
char operator;

 printf ("Enter an operator (+, -, *, /, %): ");
 scanf (" %c", &operator);

 printf ("Enter two integers: ");
 scanf ("%d %d", &num1, &num2);


  switch (operator) {
    case '+':
      sum = num1 + num2;
      printf ("%d + %d = %d", num1, num2, sum);
      break;
    case '-':
      sub = num1 - num2;
      printf ("%d - %d = %d", num1, num2, sub);
      break;
    case '*':
      mul = num1 * num2;
      printf ("%d * %d = %d", num1, num2, mul);
      break;
    case '/':
      if (num2 != 0) {
        div = (float)num1 / num2;
        printf ("%d / %d = %f", num1, num2, div);
      } else {
        printf ("Error: Division by zero is not allowed.");
      }
      break;
    case '%':
      mod = num1 % num2;
      printf ("%d %d = %d", num1, num2, mod);
      break;

    default:
      printf ("Error: Invalid operator.");
  }
return 0;

}