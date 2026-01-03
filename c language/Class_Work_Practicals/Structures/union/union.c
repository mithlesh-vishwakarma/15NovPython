#include <stdio.h>
union Student
{
  int enroll;
  char sname[30];
};

int main()
{
  union Student s1 = {123, "abc"};
  // printf("\n enter enroll & name:");
  // scanf("%d %s", &s1.enroll, s1.sname);
  printf("\n enroll=%d name=%s", s1.enroll, s1.sname);
}