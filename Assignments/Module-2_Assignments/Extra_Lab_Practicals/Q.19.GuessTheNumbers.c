// Write a C program that implements a simple number guessing game.The program should generate a random number between 1 and 100, and the user should guess the number within a limited number of attempts.Provide hints to the user if the guessed number is too high or too low.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
  int random_number, user_guess, attempts = 0;
  const int max_attempts = 10;

    srand(time(0));
  random_number = rand() % 100 + 1;

  printf("Welcome to the Number Guessing Game!\n");
  printf("I have selected a number between 1 and 100.\n");
  printf("You have %d attempts to guess the number.\n", max_attempts);

  while (attempts < max_attempts)
  {
    printf("Enter your guess: ");
    scanf("%d", &user_guess);
    attempts++;

    if (user_guess < random_number)
    {
      printf("Too low! Try again.\n");
    }
    else if (user_guess > random_number)
    {
      printf("Too high! Try again.\n");
    }
    else
    {
      printf("Congratulations! You guessed the number %d in %d attempts.\n", random_number, attempts);
      break;
    }
  }

  if (attempts == max_attempts && user_guess != random_number)
  {
    printf("Sorry, you've used all your attempts. The correct number was %d.\n", random_number);
  }

  return 0;
}