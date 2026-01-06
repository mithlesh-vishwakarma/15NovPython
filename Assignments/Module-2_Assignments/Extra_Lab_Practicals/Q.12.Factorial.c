
// Write a C program that calculates the factorial of a given number using a function. Implement both an iterative and a recursive version of the factorial function and  compare their performance for large numbers.

#include <stdio.h>
#include <time.h>
// Recursive function to calculate factorial
unsigned long long factorial_recursive(int n)
{
  if (n == 0 || n == 1)
    return 1;
  return n * factorial_recursive(n - 1);
}
// Iterative function to calculate factorial
unsigned long long factorial_iterative(int n)
{
  unsigned long long result = 1;
  for (int i = 2; i <= n; i++)
  {
    result *= i;
  }
  return result;
}
int main()
{
  int n;

  // Taking input for the number
  printf("Enter a positive integer to calculate its factorial: ");
  scanf("%d", &n);

  // Measuring time for recursive factorial
  clock_t start_recursive = clock();
  unsigned long long result_recursive = factorial_recursive(n);
  clock_t end_recursive = clock();
  double time_recursive = (double)(end_recursive - start_recursive) / CLOCKS_PER_SEC;

  // Measuring time for iterative factorial
  clock_t start_iterative = clock();
  unsigned long long result_iterative = factorial_iterative(n);
  clock_t end_iterative = clock();
  double time_iterative = (double)(end_iterative - start_iterative) / CLOCKS_PER_SEC;

  // Displaying results
  printf("Factorial of %d (recursive): %llu\n", n, result_recursive);
  printf("Time taken (recursive): %.6f seconds\n", time_recursive);

  printf("Factorial of %d (iterative): %llu\n", n, result_iterative);
  printf("Time taken (iterative): %.6f seconds\n", time_iterative);

  return 0;
}