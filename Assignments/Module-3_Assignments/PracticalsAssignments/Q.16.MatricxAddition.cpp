// Matrix Addition:
// Write a C++ program to perform matrix addition on two 2x2 matrices.
// Objective : Practice multi - dimensional arrays.

#include <iostream>
using namespace std;
int main()
{
  int matrixA[2][2], matrixB[2][2], result[2][2];

  cout << "Enter elements of Matrix A (2x2):";
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      cin >> matrixA[i][j];
    }
  }

  cout << "Enter elements of Matrix B (2x2):";
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      cin >> matrixB[i][j];
    }
  }

  // Performing matrix addition
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      result[i][j] = matrixA[i][j] + matrixB[i][j];
    }
  }

  cout << "Result of Matrix Addition (A + B):" << endl;
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      cout << result[i][j] << " ";
    }
    cout << endl;
  }

  return 0;
}