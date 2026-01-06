#include <iostream>
using namespace std;
class Maths
{
  int a, b;

public:
  Maths(int x, int y) // parameterized constructor
  {
    a = x;
    b = y;
  }
  Maths(const Maths &obj1) // copy constructor
  {
    a = obj1.a;
    b = obj1.b;
  }
  void display()
  {
    cout << "\n The value of a is: " << a;
    cout << "\n The value of b is: " << b;
  }
};
int main()
{
  Maths obj1(10, 20); // parameterized constructor called
  Maths obj2 = obj1;  // copy constructor called
  obj1.display();
  obj2.display();
  return 0;
}