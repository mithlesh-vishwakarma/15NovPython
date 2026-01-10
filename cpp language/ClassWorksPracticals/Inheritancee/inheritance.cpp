#include <iostream>
#include <string>
using namespace std;

// Parent Class
class Category
{
public:
  string categoryId;
  string categoryName;

  void getCategoryDetails()
  {
    cout << "Enter Category ID: ";
    cin >> categoryId;
    cout << "Enter Category Name: ";
    cin >> categoryName;
  }
};

// Child Class
class ProductDetails : private Category
{
public:
  int productId;
  char productName[20];
  float price;

  void getProductDetails()
  {
    getCategoryDetails(); // Accessing base class method
    cout << "Enter Product ID: ";
    cin >> productId;
    cout << "Enter Product Name: ";
    cin >> productName;
    cout << "Enter Product Price: ";
    cin >> price;
  }

  void showProductDetails()
  {
    cout << "\nProduct ID: " << productId;
    cout << "\nProduct Name: " << productName;
    cout << "\nProduct Price: " << price;
    cout << "\nCategory ID: " << categoryId;
    cout << "\nCategory Name: " << categoryName;
  }
};

int main()
{
  ProductDetails p1;

  // p1.getCategoryDetails(); // from Category // this is not accessible due to private inheritance
  p1.getProductDetails(); // from ProductDetails
  p1.showProductDetails();

  return 0;
}
