#include <iostream>
using namespace std;
class Test
{
private:
  int a, b;

public:
  Test(int a, int b)
  {
    this->a = a;
    this->b = b;
  }
  friend class FriendClass;
};
class FriendClass
{
public:
  void add(Test m)
  {
    cout << "Sum of a and b is: " << m.a + m.b << endl;
  }
};
int main()
{
  Test t1(10, 20);
  FriendClass a1;
  a1.add(t1);

  Test t2(1, 2);
  a1.add(t2);
  return 0;
}