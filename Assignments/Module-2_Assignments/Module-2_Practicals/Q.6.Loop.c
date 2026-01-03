
//  Write a C program to print numbers from 1 to 10 using all three types of loops
// (while, for, do-while).

#include <stdio.h>
int main()
{
  for (int i = 1; i <= 10; i++) // for loop
  {
    printf("%d\n", i);
  }

  int i = 1; // while loop
  while (i <= 10)
  {
    printf("%d\n", i);
    i++;
  }

  int i = 1;
  do // do while
  {
    printf("%d\n", i);
    i++;
  } while (i <= 10);
  return 0;
}
