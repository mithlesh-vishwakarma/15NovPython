#include <stdio.h>
struct subject
{
  float subname[20];
  float marks;
};
struct Student
{

  int enroll;
  char sname[20];
  struct Subject sub[3];
};
int main()
{
  int i;
  struct Student s1;
  printf("\n enter enroll no");
  scanf("%d %s", &s1.enroll, s1.sname);

  for (int i = 0; i < 3; i++)
  {
    printf("\n enter su");
  }
}