// #include <stdio.h>
// int main() {
//   int num, min = 9, digit;
//   printf("please enter the number\n");
//   scanf("%d", &num);

//   while (num > 0) {
//     digit = num % 10;
//     printf("%d\t", digit);

//     if (digit < min) {
//       min = digit;
//       printf("%d\t", min);
//     }
//     num = num / 10;
//   }
//   printf("the min is %d\n", min);
//   return 0;
// }

#include <stdio.h>

struct Student
{
  int roll;
  char name[20];
  float marks;
};

int main()
{
  struct Student s[3];
  int i;

  /* Input student details */
  for (i = 0; i < 3; i++)
  {
    printf("\nEnter details of Student %d\n", i + 1);

    printf("Roll Number: ");
    scanf("%d", &s[i].roll);

    printf("Name: ");
    scanf("%s", s[i].name);

    printf("Marks: ");
    scanf("%f", &s[i].marks);
  }

  /* Display student details */
  printf("\n--- Student Details ---\n");
  for (i = 0; i < 3; i++)
  {
    printf("\nStudent %d\n", i + 1);
    printf("Roll Number: %d\n", s[i].roll);
    printf("Name: %s\n", s[i].name);
    printf("Marks: %.2f\n", s[i].marks);
  }

  return 0;
}
