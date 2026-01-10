#include <iostream>
using namespace std;
class Account
{
public:
  double accountNumber;
  string accountHolderName;
  float balance;

  void getInfo()
  {
    cout << "Enter Account Number: ";
    cin >> accountNumber;
    cout << "Enter Account Holder Name: ";
    cin >> accountHolderName;
    cout << "Enter Balance: ";
    cin >> balance;
  }
};
class SavingsAccount : public Account
{
public:
  void getInterest()
  {
    cout << "\n the balance is:" << balance;
    balance = balance + (balance * 0.05);
  }
};
class CurrentAccount : public Account
{
public:
  void getInterest()
  {
    cout << "\n the balance is:" << balance;
    balance = balance + (balance * 0.02);
  }
};

int main()
{

  cout << "\n choose 1 for savings account \n choose 2 for current account";
  int choice;
  cin >> choice;
  if (choice == 1)
  {
    SavingsAccount s1;
    s1.getInfo();
    s1.getInterest();
    cout << "\n the total balance in savings account is:" << s1.balance << endl;
  }
  else if (choice == 2)
  {
    CurrentAccount c1;
    c1.getInfo();
    c1.getInterest();
    cout << "\n the total balance in current account is:" << c1.balance << endl;
  }
  else
  {
    cout << "invalid choice";
  }
  return 0;
};