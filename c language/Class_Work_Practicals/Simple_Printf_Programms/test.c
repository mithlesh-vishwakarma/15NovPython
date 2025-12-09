#include <stdio.h>

int main()
{
  int choice;
  float value, total = 0;
  char again = 'y';

  while (again == 'y' || again == 'Y')
  {

    printf("\nSelect option:\n");
    printf("1. Add Amount\n");
    printf("2. Subtract Amount\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    printf("Enter value: ");
    scanf("%f", &value);

    if (choice == 1)
    {
      total += value; // add to previous total
      printf("Added %.2f\n", value);
    }
    else if (choice == 2)
    {
      total -= value; // subtract from total
      printf("Subtracted %.2f\n", value);
    }
    else
    {
      printf("Invalid choice.\n");
      continue; // go back to start of loop
    }

    printf("Current total = %.2f\n", total);

    printf("Do you want to continue? (y/n): ");
    scanf(" %c", &again); // space before %c to avoid input issues
  }

  printf("\nFinal total = %.2f\n", total);
  return 0;
}
