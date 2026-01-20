#include <iostream>
using namespace std;

class Maths
{
public:
  int a, b;
  Maths(int x, int y)
  {
    a = x;
    b = y;
  }
  Maths operator+(Maths &m2) // operator overloading function
  {
    Maths m3(0, 0);
    m3.a = a + m2.a;
    m3.b = b + m2.b;
    return m3;
  }
  void display()
  {
    cout << "\na: " << a << "\tb: " << b;
  }
};
int main()
{
  Maths m1(5, 10);
  Maths m2(15, 20);
  Maths m3 = m1 + m2; // Calls the overloaded + operator
  m3.display();       // Displays the result
  return 0;
}