#include <stdio.h>
struct Student
{
  int enroll;
  char name[20];
  float per;
};

int main()
{
  struct Student s1 = {101, "Mithlesh", 89.99};
  printf("\n Enroll=%d", s1.enroll);
  printf("\n Enroll=%s", s1.name);
  printf("\n Enroll=%.2f", s1.per);

  return 0;
}
