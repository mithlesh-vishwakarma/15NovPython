#include <iostream>
using namespace std;
class A
{
public:
  int a;
  void getA()
  {
    cout << "\n enter a";
    cin >> a;
  }
};
class B
{
public:
  int b;
  void getB()
  {
    cout << "\n enter b";
    cin >> b;
  }
};
class C : public A, public B
{
public:
  int c;
  void getC()
  {
    cout << "\n enter c";
    cin >> c;
  }
  void Add()
  {
    cout << "\n sum is " << a + b + c;
  }
};
int main()
{
  C obj;
  obj.getA();
  obj.getB();
  obj.getC();
  obj.Add();
  return 0;
}