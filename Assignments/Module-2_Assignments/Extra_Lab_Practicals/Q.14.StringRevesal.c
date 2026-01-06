// Write a C program that takes a string as input and reverses it using a function.Write the program without using built - in string handling functions.

#include <stdio.h>
void reverse_string(char str[], char reversed[])
{
  int length = 0;

  while (str[length] != '\0')
  {
    length++;
  }

  for (int i = 0; i < length; i++)
  {
    reversed[i] = str[length - 1 - i];
  }
  reversed[length] = '\0';
}
int main()
{
  char str[100], reversed[100];

  printf("Enter a string: ");
  scanf("%s", str);

  reverse_string(str, reversed);

  printf("Reversed string: %s\n", reversed);

  return 0;
}