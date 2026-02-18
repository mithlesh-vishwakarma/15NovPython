#include <iostream>
#include <fstream>
using namespace std;
main()
{

  fstream w1;
  char name[20];
  int age;
  char sub[20], ch;
  w1.open("file.csv", ios::out);
  for (int i = 0; i < 3; i++)
  {
    cout << "Enter name:,age:, and Sub; ";
    cin >> name >> age >> sub;
    w1 << name << " ," << age << ", " << sub << endl;
  }

  w1.close();
  fstream r1;
  r1.open("file.csv", ios::in);

  while (r1.get(ch))
  {
    if (ch == ',')
    {

      cout << "\t";
      continue;
    }
    cout << ch;
  }

  if (r1.eof())
  {

    cout << "File end here \n";
  }
  r1.close();
}