// Write a C program that takes a number as input and checks whether it is a palindrome using a function.Modify the program to check if a given string is a palindrome.

#include <stdio.h>
#include <string.h>
// Function to check if a number is a palindrome
int is_number_palindrome(int num)
{
  int reversed = 0, original = num, remainder;
  while (num != 0)
  {
    remainder = num % 10;
    reversed = reversed * 10 + remainder;
    num /= 10;
  }
  return original == reversed;
}
// Function to check if a string is a palindrome
int is_string_palindrome(char str[])
{
  int left = 0;
  int right = strlen(str) - 1;
  while (left < right)
  {
    if (str[left] != str[right])
      return 0;
    left++;
    right--;
  }
  return 1;
}
int main()
{
  int choice;
  printf("Choose an option:\n1. Check number palindrome\n2. Check string palindrome\n");
  scanf("%d", &choice);

  if (choice == 1)
  {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    if (is_number_palindrome(num))
      printf("%d is a palindrome number.\n", num);
    else
      printf("%d is not a palindrome number.\n", num);
  }
  else if (choice == 2)
  {
    char str[100];
    printf("Enter a string: ");
    scanf("%s", str);
    if (is_string_palindrome(str))
      printf("\"%s\" is a palindrome string.\n", str);
    else
      printf("\"%s\" is not a palindrome string.\n", str);
  }
  else
  {
    printf("Invalid choice.\n");
  }

  return 0;
}