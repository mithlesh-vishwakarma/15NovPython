#include <stdio.h>
struct Student
{
  int enroll;
  char name[20];
  float per;
};

int main()
{
  struct Student s1;

  printf("\n enter the values of Enrollment,name,And Per");
  scanf("%d %s %f", &s1.enroll, s1.name, &s1.per);

  printf("\n Enroll=%d", s1.enroll);
  printf("\n Enroll=%s", s1.name);
  printf("\n Enroll=%.2f", s1.per);

  return 0;
}
