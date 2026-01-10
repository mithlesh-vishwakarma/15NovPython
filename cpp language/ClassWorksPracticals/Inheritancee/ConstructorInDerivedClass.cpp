#include <iostream>
using namespace std;
class parent
{
public:
  int a, b;
  parent() // parent class constructor
  {
    cout << "Parent class constructor called." << endl;
  }
  parent(int x, int y) // parameterized constructor
  {
    a = x;
    b = y;
    cout << "value of a=" << a << "value of b=" << b << endl;
  }
};

class child : public parent
{
public:
  int c;
  child()
  {
    cout << "Child class constructor called." << endl;
  }

  child(int x, int y, int z) : parent(x, y)
  {
    c = z;
    cout << "value of c=" << c << endl;
  }
};

int main()

{
  child obj1;
  child(12, 13, 14);
  return 0;
}