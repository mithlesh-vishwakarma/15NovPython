// Class for Bank Account
// Create a class BankAccount with data members like balance and member functions
// like deposit and withdraw. Implement encapsulation by keeping the data members
// private.
// Objective: Understand encapsulation in classes.

#include <iostream>
using namespace std;
class BankAccount
{
private:
  double balance;

public:
  BankAccount() : balance(0) {}

  void deposit(double amount)
  {
    if (amount > 0)
    {
      balance += amount;
      cout << "\nDeposited: " << amount;
    }
    else
    {
      cout << "\nInvalid deposit amount!";
    }
  }

  void withdraw(double amount)
  {
    if (amount > 0 && amount <= balance)
    {
      balance -= amount;
      cout << "\nWithdrawn: " << amount;
    }
    else
    {
      cout << "\nInvalid withdrawal amount or insufficient funds!";
    }
  }

  double getBalance() const
  {
    return balance;
  }
};
int main()
{
  BankAccount account;

  account.deposit(1000);
  cout << "\nCurrent Balance: " << account.getBalance();

  account.withdraw(500);
  cout << "\nCurrent Balance: " << account.getBalance();

  account.withdraw(600); // Attempt to withdraw more than the balance
  cout << "\nCurrent Balance: " << account.getBalance();

  return 0;
}