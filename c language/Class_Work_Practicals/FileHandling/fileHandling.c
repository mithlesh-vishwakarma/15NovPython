#include <stdio.h>
int main()
{
  char data[50];
  FILE *fp;
  fp = fopen("hello.txt", "w");
  fprintf(fp, "hii, this is mithlesh here. i am writing in the file.");
  fclose(fp);
  fp = fopen("hello.txt", "r");
  fgets(data, 54, fp);
  printf("\n reading data from file=%s", data);
  fclose(fp);

  return 0;
}