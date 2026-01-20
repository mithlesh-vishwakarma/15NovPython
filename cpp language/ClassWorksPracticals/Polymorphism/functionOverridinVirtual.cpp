#include <iostream>
using namespace std;

class Parent
{
public:
  virtual void display() = 0; // Pure virtual function
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
