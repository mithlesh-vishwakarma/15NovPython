#include <iostream>
using namespace std;
class Maths
{
  int a, b, c, d;

public:
  ~Maths()
  {
    // Destructor
    cout << "\nDestructor called for object with values: " << a << ", " << b << ", " << c << ", " << d;
  }
  Maths(int x, int y, int z, int w) // parameterized constructor
  {
    a = x;
    b = y;
    c = z;
    d = w;
  }
  Maths(const Maths &obj1) // copy constructor
  {
    a = obj1.a;
    b = obj1.b;
    c = obj1.c;
    d = obj1.d;
  }

  void display()
  {
    cout << "\n The value of a is: " << a;
    cout << "\n The value of b is: " << b;
    cout << "\n The value of c is: " << c;
    cout << "\n The value of d is: " << d;
  }
};
int main()
{
  Maths m1(10, 20, 30, 40); // parameterized constructor called
  m1.display();
  Maths *obj2 = new Maths(333, 444, 555, 666); // dynamic object creation
  obj2->display();                             // showing values of obj2
  return 0;
}