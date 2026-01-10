#include <iostream>
using namespace std;
class maths
{
public:
  void add(int a, int b)
  {
    cout << "Sum of two integers: " << a + b << endl;
  }
  void add(double a, double b)
  {
    cout << "Sum of two doubles: " << a + b << endl;
  }
  void add(int a, int b, int c)
  {
    cout << "Sum of three integers: " << a + b + c << endl;
  }
};
int main()
{
  maths m;
  m.add(5, 10);     // Calls the first add function
  m.add(5.5, 10.2); // Calls the second add function
  m.add(1, 2, 3);   // Calls the third add function
  return 0;
}