#include <stdio.h>
int main()
{
  int enroll;
  char name[20];
  FILE *fp;
  printf("\n Enter Enroll and Name: ");
  scanf("%d %s", &enroll, name);
  fp = fopen("Student.csv", "w");
  fprintf(fp, "Enrollment Id=%d and name=%s", enroll, name);
  fclose(fp);

  // reading...

  fp = fopen("Student.csv", "r");
  scanf("%d %s", &enroll, name);
  printf("\nEnrollment Id = % d and name = % s", enroll, name);
  return 0;
}