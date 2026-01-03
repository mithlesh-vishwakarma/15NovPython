// Write a C program that acts as a simple calculator.The program should take two numbers and an operator as input from the user and perform the respective operation(addition,subtraction, multiplication, division, or modulus) using operators.
// Challenge : Extend the program to handle invalid operator inputs.

#include <stdio.h>

int main()
{
  char op;
  double num1, num2;
  int intResult;

  printf("Enter first number: ");
  scanf("%lf", &num1);

  printf("Enter an operator (+, -, *, /, %%): ");
  scanf(" %c", &op);

  printf("Enter second number: ");
  scanf("%lf", &num2);

  switch (op)
  {
  case '+':
    printf("%.2f + %.2f = %.2f\n", num1, num2, num1 + num2);
    break;

  case '-':
    printf("%.2f - %.2f = %.2f\n", num1, num2, num1 - num2);
    break;

  case '*':
    printf("%.2f * %.2f = %.2f\n", num1, num2, num1 * num2);
    break;

  case '/':
    if (num2 != 0)
      printf("%.2f / %.2f = %.2f\n", num1, num2, num1 / num2);
    else
      printf("Error: Division by zero is not allowed.\n");
    break;

  case '%':
    if ((int)num2 != 0)
    {
      intResult = (int)num1 % (int)num2;
      printf("%d %% %d = %d\n", (int)num1, (int)num2, intResult);
    }
    else
      printf("Error: Modulus by zero is not allowed.\n");
    break;

  default:
    printf("Error: Invalid operator.\n");
  }

  return 0;
}
