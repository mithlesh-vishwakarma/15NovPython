#include <stdio.h>
int main()
{
  char str[] = {'M', 'I', 'T', 'H', 'L', 'E', 'S', 'H', '\0'};
  // char name[20];
  char name2[20];
  printf("%s\n", str);
  // printf("enter the value of str\n");
  // scanf("%s", name);
  // printf("%s", name);
  gets(name2);
  puts(name2);

  return 0;
}