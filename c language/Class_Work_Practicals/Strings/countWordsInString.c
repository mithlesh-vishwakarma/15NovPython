#include <stdio.h>

int main()
{
  char str[200];
  int i = 0;
  int characters = 0;
  int alphabets = 0;
  int words = 0;

  printf("Enter a sentence:\n");
  gets(str); // takes input including spaces

  puts("\nYou entered:");
  puts(str);

  while (str[i] != '\0')
  {
    characters++;

    // check alphabet
    if ((str[i] >= 'A' && str[i] <= 'Z') ||
        (str[i] >= 'a' && str[i] <= 'z'))
    {
      alphabets++;
    }

    // check word (space followed by a character)
    if (str[i] == ' ' && str[i + 1] != ' ' && str[i + 1] != '\0')
    {
      words++;
    }

    i++;
  }

  // if sentence is not empty, words = spaces + 1
  if (characters > 0)
  {
    words = words + 1;
  }

  printf("\nTotal Characters = %d", characters);
  printf("\nTotal Alphabets  = %d", alphabets);
  printf("\nTotal Words      = %d", words);

  return 0;
}
