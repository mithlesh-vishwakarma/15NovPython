// Write a C program that accepts 10 integers from the user and stores them in an array.The
// program should then find and print the maximum and minimum values in the array.Challenge : Extend the program to sort the array in ascending order.

#include <stdio.h>
int main()
{
  int arr[10];
  int max, min, temp;

  // Taking input from the user
  printf("Enter 10 integers:\n");
  for (int i = 0; i < 10; i++)
  {
    scanf("%d", &arr[i]);
  }

  // Initialize max and min with the first element of the array
  max = arr[0];
  min = arr[0];

  // Find maximum and minimum values in the array
  for (int i = 1; i < 10; i++)
  {
    if (arr[i] > max)
      max = arr[i];
    if (arr[i] < min)
      min = arr[i];
  }

  // Display the maximum and minimum values
  printf("Maximum value: %d\n", max);
  printf("Minimum value: %d\n", min);

  // sort the array in ascending order.
  for (int i = 0; i < 9; i++)
  {
    for (int j = 0; j < 9 - i; j++)
    {
      if (arr[j] > arr[j + 1])
      {

        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }

  // Display the sorted array
  printf("Sorted array in ascending order:\n");
  for (int i = 0; i < 10; i++)
  {
    printf("%d ", arr[i]);
  }
  printf("\n");

  return 0;
}