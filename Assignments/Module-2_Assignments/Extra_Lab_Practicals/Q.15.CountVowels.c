// Write a C program that takes a string from the user and counts the number of
// vowels, consonants, digits, and special characters.

#include <stdio.h>

int main()
{
  char str[100];
  int vowels = 0, consonants = 0, digits = 0, special_chars = 0;
  int i = 0;

  // Taking input for the string
  printf("Enter a string: ");
  fgets(str, sizeof(str), stdin);

  while (str[i] != '\0')
  {
    char ch = str[i];

    if ((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z'))
    {

      if (ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U' ||
          ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
      {
        vowels++;
      }
      else
      {
        consonants++;
      }
    }

    else if (ch >= '0' && ch <= '9')
    {
      digits++;
    }

    else if (ch != ' ' && ch != '\n')
    {
      special_chars++;
    }

    i++;
  }

  printf("Vowels: %d\n", vowels);
  printf("Consonants: %d\n", consonants);
  printf("Digits: %d\n", digits);
  printf("Special Characters: %d\n", special_chars);

  return 0;
}
