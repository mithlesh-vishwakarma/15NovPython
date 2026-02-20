// 3. POP vs.OOP Comparison Program :
// Write two small programs : one using Procedural Programming(POP) to calculate the area of a rectangle,and another using Object - Oriented Programming(OOP) with a class and object for the same task.
// Objective: Highlight the difference between POP and OOP approaches.

#include <iostream>
using namespace std;

float areaOfRectangle;

// Procedural Programming Approach

void calculateAreaPOP(float length, float width)
{
  areaOfRectangle = length * width;
  cout << "\nPOP Area of Rectangle: " << areaOfRectangle;
}

// Object-Oriented Programming Approach
class Rectangle
{
public:
  float length;
  float width;

public:
  void setDimensions(float l, float w)
  {
    length = l;
    width = w;
  }

  float calculateAreaOOP()
  {

    return length * width;
  }
};

int main()
{

  // POP Approach
  float length, width;
  cout << "\n Enter the length of rectangle: ";
  cin >> length;
  cout << "\n Enter the width of rectangle: ";
  cin >> width;

  calculateAreaPOP(length, width);

  // oop approach

  Rectangle obj;
  obj.setDimensions(length, width);
  cout << "\nOOP Area of Rectangle: ";
  cout << obj.calculateAreaOOP();
  return 0;
}