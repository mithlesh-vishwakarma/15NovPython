#include <iostream>
#include <string>
using namespace std;

// Parent Class
class ProductDetails
{
public:
  int productId, quantity;
  char productName[20];
  float price;

public:
  void getProductDetails()
  {
    cout << "Enter Product ID: ";
    cin >> productId;
    cout << "Enter Product Name: ";
    cin >> productName;
    cout << "Enter Product Price: ";
    cin >> price;
    cout << "Enter Quantity: ";
    cin >> quantity;
  }
};
// parent Class

class User
{
public:
  int userId;
  string userName;

public:
  void userData()
  {
    cout << "\n enter UserID:" << userId;
    cin >> userId;
    cout << "\n enter UserName:" << userName;
    cin >> userName;
  }
};

class Cart : public ProductDetails, public User
{
public:
  int cartId;

  void showCartDetails()
  {
    cout << "\n Enter Cart ID: ";
    cin >> cartId;
    cout << "\n Cart ID: " << cartId;
    cout << "\n User ID: " << userId;
    cout << "\n User Name: " << userName;
    cout << "\n Product ID: " << productId;
    cout << "\n Product Name: " << productName;
    cout << "\n Product Price: " << price;
    cout << "\n Total Price: " << price * quantity;
  }
};

int main()
{
  Cart c1;
  c1.showCartDetails();

  return 0;
}
