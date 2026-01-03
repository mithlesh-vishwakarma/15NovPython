#include <stdio.h>
int main()
{
  int uid;
  char uname[20], ch;
  char email[20];
  FILE *fp;
  fp = fopen("user.csv", "a"); // change the value of w into the append -a
  fprintf(fp, "UserID, UserName, Email\n");
  for (int i = 0; i < 2; i++)
  {
    printf("enter the uid name and email\n");
    scanf("%d %s %s", &uid, uname, email);
    fprintf(fp, " %d, %s, %s", uid, uname, email);
  }
  fclose(fp);
  /// reading

  fp = fopen("user.csv", "r");
  while ((ch = getc(fp)) != EOF)
  {
    if (ch == ',')
    {
      putchar('\t');
      continue;
    }
    putchar(ch);
  }

  return 0;
}