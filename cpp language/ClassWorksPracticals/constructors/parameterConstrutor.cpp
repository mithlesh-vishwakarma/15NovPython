#include <iostream>
#include <string.h>
using namespace std;
class User
{
public:
  char username[20];
  char email[30];
  char contact[15];

  User(const char uname[20], char em[30], char cont[15])
  {
    strcpy(username, uname);
    strcpy(email, em);
    strcpy(contact, cont);
  };
  void showUser()
  {
    cout << "\n Username: " << username;
    cout << "\n Email: " << email;
    cout << "\n Contact: " << contact;
  };
};

int main()
{
  User u1("mithlesh", "mithlesh@gmail.com", "9876543210");
  u1.showUser();
}