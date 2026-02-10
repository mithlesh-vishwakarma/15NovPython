// Inheritance Example
// Write a program that implements inheritance using a base class Person and derived
// classes Student and Teacher.Demonstrate reusability through inheritance.
// Objective : Learn the concept of inheritance.

#include <iostream>
using namespace std;
class Person
{
public:
  void display()
  {
    cout << "This is a person.";
  }
};
class Student : public Person
{
public:
  void display()
  {
    cout << "This is a student.";
  }
};
int main()
{
  Person person;
  Student student;

  person.display();  // Output: This is a person.
  student.display(); // Output: This is a student.

  return 0;
}