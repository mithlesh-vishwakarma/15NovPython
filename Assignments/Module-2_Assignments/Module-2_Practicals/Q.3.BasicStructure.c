// Write a C program that includes variables, constants, and comments.Declare and use different data types(int, char, float) and display their values.

#include <stdio.h>
int main()
{
  // Variable declarations
  int intVar = 10;       // Integer variable
  char charVar = 'A';    // Character variable
  float floatVar = 5.5f; // Float variable

  // Constant declaration
  const int CONST_VAR = 100; // Constant integer

  // Displaying values
  printf("Integer Variable: %d\n", intVar);
  printf("Character Variable: %c\n", charVar);
  printf("Float Variable: %.2f\n", floatVar);
  printf("Constant Variable: %d\n", CONST_VAR);

  return 0;
}