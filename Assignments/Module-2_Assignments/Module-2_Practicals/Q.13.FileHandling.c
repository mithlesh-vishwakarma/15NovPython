// Write a C program to create a file, write a string into it, close the file, then open the file again to read and display its contents.

#include <stdio.h>
int main()
{
  FILE *filePtr;
  char strToWrite[] = "Hello, this is a sample string written to the file.";
  char strToRead[100];

  // Create and write to the file
  filePtr = fopen("sample.txt", "w");
  if (filePtr == NULL)
  {
    printf("Error opening file for writing.\n");
    return 1;
  }
  fprintf(filePtr, "%s\n", strToWrite);
  fclose(filePtr);

  // Open the file again to read its contents
  filePtr = fopen("sample.txt", "r");
  if (filePtr == NULL)
  {
    printf("Error opening file for reading.\n");
    return 1;
  }
  printf("Contents of the file:\n");
  while (fgets(strToRead, sizeof(strToRead), filePtr) != NULL)
  {
    printf("%s", strToRead);
  }
  fclose(filePtr);

  return 0;
}