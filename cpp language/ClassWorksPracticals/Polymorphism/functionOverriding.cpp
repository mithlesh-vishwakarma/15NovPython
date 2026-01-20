#include <iostream>
using namespace std;

class Parent
{
public:
  void display()
  {
    cout << "Parent class show function called.";
  }
  // void display()
  // {
  //   cout << "Parent class show function called.";
  // }
};
class child : public Parent
{
public:
  void display()
  {
    cout << "Child class show function called.";
  }
};

int main()
{
  child c;
  c.display(); // Calls the child class display function
  return 0;
}
