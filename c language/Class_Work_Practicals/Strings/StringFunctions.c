#include <stdio.h>
#include <string.h>
int main()
{
  char str1[20], str2[20];
  printf("please enter the str1");
  scanf("%s", str1);

  printf("string length :%d\n", strlen(str1));
  strcpy(str2, str1);
  printf("string copied to str2 :%s\n", str2);
  strupr(str2);
  printf("str2 in upper case:%s\n", str2);
  strrev(str1);
  printf("str1 reverse :%s\n", str1);
  strcat(str1, str2);
  printf("Here is the concateneted str:%s\n", str1);

  return 0;
}