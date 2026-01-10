#include <iostream>
using namespace std;

class A
{
public:
  int a;
  void getA()
  {
    cout << "\nEnter a: ";
    cin >> a;
  }
};

class B : virtual public A
{
public:
  int b;
  void getB()
  {
    cout << "\nEnter b: ";
    cin >> b;
  }
};

class C : virtual public A
{
public:
  int c;
  void getC()
  {
    cout << "\nEnter c: ";
    cin >> c;
  }
};

class D : public B, public C
{
public:
  int d;
  void getD()
  {
    cout << "\nEnter d: ";
    cin >> d;
  }

  void Add()
  {
    cout << "\nSum is: " << a + b + c + d;
  }
};

int main()
{
  D obj;
  obj.getA();
  obj.getB();
  obj.getC();
  obj.getD();
  obj.Add();
  return 0;
}
