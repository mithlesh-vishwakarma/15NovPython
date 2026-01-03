/*Write a C program to check if a number is even or odd using an if-else
statement. Extend the program using a switch statement to display the month
name based on the user’s input (1 for January, 2 for February, etc.).*/

#include <stdio.h>
int main()
{
  int num;
  printf("please enter a number:\n");
  scanf("%d", &num);
  if (num % 2 == 0)
  {
    printf("number is even");
  }
  else
  {
    printf("the number is odd");
  }

  return 0;
}

/*
Output:

please enter a number:
34
number is even

*/

#include <stdio.h>
int main()
{
  char choice;
  printf("please enter the choice:\n");
  printf("1. January\n"
         "2. february\n"
         "3. March\n"
         "4. April\n"
         "5. May\n"
         "6. June\n"
         "7. July\n"
         "8. August\n"
         "9. September\n"
         "10. October\n"
         "11. November\n"
         "12. December\n");
  scanf("%c", &choice);

  switch (choice)
  {
  case '1':
    printf("you have selected January !\n");
    break;
  case '2':
    printf("you have selected febuary !\n");
    break;
  case '3':
    printf("you have selected March !\n");
    break;
  case '4':
    printf("you have selected April !\n");
    break;
  case '5':
    printf("you have selected May !\n");
    break;
  case '6':
    printf("you have selected June !\n");
    break;
  case '7':
    printf("you have selected July !\n");
    break;
  case '8':
    printf("you have selected August !\n");
    break;
  case '9':
    printf("you have selected September !\n");
    break;
  case '10':
    printf("you have selected October !\n");
    break;
  case '11':
    printf("you have selected November !\n");
    break;
  case '12':
    printf("you have selected December !\n");
    break;
  default:
    printf("please enter valid input this is invalid !!");
  }
}

/*
output:
-------

please enter the choice:
1. January
2. february
3. March
4. April
5. May
6. June
7. July
8. August
9. September
10. October
11. November
12. December
4
you have selected April !

*/