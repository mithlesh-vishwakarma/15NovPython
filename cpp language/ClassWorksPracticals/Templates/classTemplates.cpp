#include <iostream>
using namespace std;
int i, j;
template <class T>
class Sort
{
public:
  T a[5], temp;
  void input()
  {
    cout << "Enter 5 elements: ";
    for (i = 0; i < 5; i++)
    {
      cout << "Element a[" << i << "]: ";
      cin >> a[i];
    }
  }
  void sortArray()
  {
    for (i = 0; i < 5; i++)
    {
      for (j = i + 1; j < 5; j++)
      {
        if (a[i] > a[j])
        {
          temp = a[i];
          a[i] = a[j];
          a[j] = temp;
        }
      }
    }
  }
  void printArray()
  {
    cout << "Sorted array: ";
    for (i = 0; i < 5; i++)
    {
      cout << a[i] << " ";
    }
    cout << endl;
  }
};
int main()
{
  Sort<int> s1;
  s1.input();
  s1.sortArray();
  s1.printArray();

  Sort<char> s2;
  s2.input();
  s2.sortArray();
  s2.printArray();

  return 0;
}