// Create a lecture management System
// Make sure each business logic is denoted with appropriate comments and
// make your code interactive and represent clean and clear output on your
// console screen.

// Adhere to the coding principles
// Define a class to represent lecture details. Include the following members and the
// program should handle at least details of 5 lecturers.
// Data members:
// a) Name of the lecturer
// b) Name of the subject
// c) Name of course
// d) Number of lecturers
// Data functions:
// a) To assign initial values
// b) To add a lecture details
// c) To display name and lecture details
// Make sure you have to use constructor concept in it
// Make sure all naming conversion properly mention in this project work
// Make sure all method name
// Use class and object concepts
// Upload all features in develop branch after completion all features
// merge it with the main branch.

#include <iostream>
#include <string>
using namespace std;
class Lecturer
{
private:
  string name;
  string subject;
  string course;

public:
  Lecturer(string n, string s, string c) : name(n), subject(s), course(c) {}

  void displayDetails()
  {
    cout << "\nLecturer Name: " << name;
    cout << "\nSubject: " << subject;
    cout << "\nCourse: " << course;
  }
};
int main()
{
  Lecturer lecturers[5] = {
      Lecturer("\nDr. Smith", "Mathematics", "Calculus"),
      Lecturer("\nProf. Johnson", "Computer Science", "Data Structures"),
      Lecturer("\nDr. Brown", "Physics", "Quantum Mechanics"),
      Lecturer("\nProf. Davis", "Chemistry", "Organic Chemistry"),
      Lecturer("\nDr. Wilson", "Biology", "Genetics")};

  cout << "Lecture Details:\n";
  for (int i = 0; i < 5; i++)
  {
    cout << "\nLecturer " << (i + 1) << ":\n";
    lecturers[i].displayDetails();
  }

  return 0;
}