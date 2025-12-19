#include <stdio.h>
int main()
{
  char str[20], rev[20];
  int i = 0, j = 0;
  printf("\n enter string:");
  scanf("%s", str);
  printf("\n str=%s", str);
  while (str[i] != '\0')
  {
    i++; // checks the counts of string;
  }
  printf("\n lenth of str= %d", i);

  ////-------------------------------------------------------------
  i--;
  printf("\n reverse string task------", rev);
  while (i >= 0)
  {
    rev[j] = str[i];
    i--;
    j++;
  }
  rev[j] = '\0';
  printf("\n rev Str=%s", rev);

  return 0;
}