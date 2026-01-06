// Write a C program that generates the Fibonacci sequence up to N terms using a recursive function.Modify the program to calculate the Nth Fibonacci number using both iterative and recursive methods.Compare their efficiency.

#include <stdio.h>
// Recursive function to calculate Fibonacci number
int fibonacci_recursive(int n)
{
  if (n <= 1)
    return n;
  return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

// Iterative function to calculate Fibonacci number
int fibonacci_iterative(int n)
{
  if (n <= 1)
    return n;
  int a = 0, b = 1, fib;
  for (int i = 2; i <= n; i++)
  {
    fib = a + b;
    a = b;
    b = fib;
  }
  return fib;
}
int main()
{
  int n;

  // Taking input for the number of terms
  printf("Enter the number of terms in Fibonacci sequence: ");
  scanf("%d", &n);

  // Generating Fibonacci sequence using recursive method
  printf("Fibonacci sequence (recursive):\n");
  for (int i = 0; i < n; i++)
  {
    printf("%d ", fibonacci_recursive(i));
  }
  printf("\n");

  // Generating Fibonacci sequence using iterative method
  printf("Fibonacci sequence (iterative):\n");
  for (int i = 0; i < n; i++)
  {
    printf("%d ", fibonacci_iterative(i));
  }
  printf("\n");

  // Calculating Nth Fibonacci number using both methods
  int nth_fib_recursive = fibonacci_recursive(n - 1);
  int nth_fib_iterative = fibonacci_iterative(n - 1);

  // Displaying the Nth Fibonacci number
  printf("Nth Fibonacci number (recursive): %d\n", nth_fib_recursive);
  printf("Nth Fibonacci number (iterative): %d\n", nth_fib_iterative);

  return 0;
}