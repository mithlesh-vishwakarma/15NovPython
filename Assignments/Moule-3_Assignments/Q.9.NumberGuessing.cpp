// Number Guessing Game: Write a C++ program that asks the user to guess a number between 1 and 100. The program should provide hints if the guess is too high or too low.Use loops to allow the user multiple attempts.o Objective : Understand while loops and conditional logic.

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main()
{
  // Seed the random number generator
  srand(static_cast<unsigned int>(time(0)));
  int secretNumber = rand() % 100 + 1; // Random number between 1 and 100
  int userGuess = 0;
  int attempts = 0;

  cout << "Welcome to the Number Guessing Game!";
  cout << "I have selected a number between 1 and 100.";
  cout << "Can you guess what it is?";

  // Loop until the user guesses the correct number
  while (userGuess != secretNumber)
  {
    cout << "Enter your guess: ";
    cin >> userGuess;
    attempts++;

    if (userGuess < secretNumber)
    {
      cout << "Too low! Try again.";
    }
    else if (userGuess > secretNumber)
    {
      cout << "Too high! Try again.";
    }
    else
    {
      cout << "Congratulations! You've guessed the number " << secretNumber << " in " << attempts << " attempts.";
    }
  }

  return 0;
}