#include <iostream>
using namespace std;
class User
{
  int uid;
  char uname[20];
  char email[30];
  double contact;

public:
  void getUserData()
  {
    cout << "\n User ID: ";
    cout << "\n User Name: ";
    cout << "\n User Email: ";
    cout << "\n User Contact: ";
    cin >> uid >> uname >> email >> contact;
  }
  void displayUserData()
  {
    cout << "\nUser ID: " << uid;
    cout << "\nUser Name: " << uname;
    cout << "\nUser Email: " << email;
    cout << "\nUser Contact: " << contact;
  }
};

int main()
{
  User u1;
  u1.getUserData();
  u1.displayUserData();
  return 0;
}