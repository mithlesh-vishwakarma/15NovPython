#include <stdio.h>
struct Student
{
  int enroll;
  char name[20];
  float per;
};

int main()
{
  struct Student s[5];
  int i;
  for (i = 0; i < 5; i++)
  {

    printf("\n enter the values of Enrollment,name,And Per");
    scanf("%d %s %f", &s[i].enroll, s[i].name, &s[i].per);
  }

  for (i = 0; i < 5; i++)
  {

    printf("\n Enroll=%d", s[i].enroll);
    printf("\t Enroll=%s", s[i].name);
    printf("\t Enroll=%.2f", s[i].per);
  }

  return 0;
}
