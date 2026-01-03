// Write a C program that takes two strings from the user and concatenates them using strcat().Display the concatenated string and its length using strlen().

#include <stdio.h>
#include <string.h>
int main()
{
  char str1[100], str2[100], concatenated[200];
  printf("Enter first string: ");
  fgets(str1, sizeof(str1), stdin);
  str1[strcspn(str1, "\n")] = 0; // Remove newline character if present

  printf("Enter second string: ");
  fgets(str2, sizeof(str2), stdin);
  str2[strcspn(str2, "\n")] = 0; // Remove newline character if present

  strcpy(concatenated, str1); // Copy first string to concatenated
  strcat(concatenated, str2); // Append second string to concatenated

  // Display concatenated string and its length
  printf("Concatenated String: %s\n", concatenated);
  printf("Length of Concatenated String: %lu\n", strlen(concatenated));

  return 0;
}