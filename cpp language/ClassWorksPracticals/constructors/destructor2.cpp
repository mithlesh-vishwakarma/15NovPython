#include <iostream>
using namespace std;
class sample
{
  int a;

public:
  sample() // constructor
  {
    a = 10;
  }
  ~sample() // destructor
  {
    cout << "\nDestructor called for object with value: " << a;
  }

  void display()
  {
    cout << "The value of a is: " << a;
  }
  void showData()
  {
    cout << "The value of a is: " << a;
  }
};
int main()
{
  sample obj;    // object creation
  obj.display(); // function call
  obj.showData();
  return 0;
}