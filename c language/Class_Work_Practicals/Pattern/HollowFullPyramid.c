// #include <stdio.h>
// int main()
// {

//   for (int i = 1; i <= 10; i++)
//   {

//     for (int k = 1; k <= i; k++)
//     {
//       if (k == i)
//       {
//         printf("*");
//       }
//       printf(" ");
//     }
//     for (int j = 10; j >= i; j--)
//     {
//       if (i == 1 || j == i)
//       {
//         printf("* ");
//       }
//       else
//       {
//         printf(" ");
//       }
//     }

//     printf("\n");
//   }

//   return 0;
// }

#include <stdio.h>
int main()
{
  for (int i = 1; i <= 6; i++)
  {
    for (int k = 6; k >= i; k--)
    {
      if (k != i)
      {
        printf(" ");
      }
      // else
      // {
      //   printf("* ");
      // }
    }
    for (int j = 1; j <= i; j++)
    {
      if (i == 6 || j == i || j == 1)
      {
        printf("* ");
      }
      else
      {
        printf("  ");
      }
    }

    printf("\n");
  }

  return 0;
}

/*

output

     *
    * *
   *   *
  *     *
 *       *
* * * * * *

*/