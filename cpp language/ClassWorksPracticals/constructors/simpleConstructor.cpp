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
  void display()
  {
    cout << "The value of a is: " << a << endl;
  }
};
int main()
{
  sample obj;    // object creation
  obj.display(); // function call
  return 0;
}