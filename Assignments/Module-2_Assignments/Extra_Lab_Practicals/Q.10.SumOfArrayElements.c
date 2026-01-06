// Write a C program that takes N numbers from the user and stores them in an array.The program should then calculate and display the sum of all array elements.Modify the program to also find the average of the numbers.

#include <stdio.h>
int main()
{
  int n, sum = 0;
  float average;

  // Taking input for the number of elements
  printf("Enter the number of elements: ");
  scanf("%d", &n);

  int arr[n];

  // Taking input for the array elements
  printf("Enter %d integers:\n", n);
  for (int i = 0; i < n; i++)
  {
    scanf("%d", &arr[i]);
  }

  // Calculating the sum of array elements
  for (int i = 0; i < n; i++)
  {
    sum += arr[i];
  }

  // Calculating the average
  average = (float)sum / n;

  // Displaying the sum and average
  printf("Sum of array elements: %d\n", sum);
  printf("Average of array elements: %.2f\n", average);

  return 0;
}