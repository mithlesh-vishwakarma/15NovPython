#include <iostream>
using namespace std;
template <typename T>
T calc(T a, T b)
{
  cout << "Sum of a and b is: " << a + b << endl;
  cout << "Difference of a and b is: " << a - b << endl;
  cout << "Product of a and b is: " << a * b << endl;
  cout << "Quotient of a and b is: " << a / b << endl;
}
int main()
{
  calc<int>(10, 20);
  calc<float>(1.5, 2.5);
  return 0;
}
