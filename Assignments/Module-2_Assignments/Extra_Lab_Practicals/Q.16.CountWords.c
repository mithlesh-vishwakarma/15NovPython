// Write a C program that counts the number of words in a sentence entered by the user.Modify the program to find the longest word in the sentence.

#include <stdio.h>
#include <string.h>
#define MAX_LENGTH 1000
int main()
{
  char str[MAX_LENGTH];
  int word_count = 0;
  char longest_word[MAX_LENGTH] = "";
  char current_word[MAX_LENGTH] = "";
  int i = 0, j = 0;

  printf("Enter a sentence: ");
  fgets(str, sizeof(str), stdin);

  while (1)
  {
    char ch = str[i];

    if (ch != ' ' && ch != '\n' && ch != '\0')
    {
      current_word[j++] = ch;
    }
    else
    {
      if (j > 0)
      {
        current_word[j] = '\0';
        word_count++;

        if (strlen(current_word) > strlen(longest_word))
        {
          strcpy(longest_word, current_word);
        }

        j = 0; // Reset for the next word
      }

      if (ch == '\0')
        break;
    }
    i++;
  }

  // Displaying the results
  printf("Number of words: %d\n", word_count);
  printf("Longest word: %s\n", longest_word);

  return 0;
}