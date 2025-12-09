/* C Programming Assessment Test
-------------------------------------
• Write a program to demonstrate a Food Billing System.
• Display the Menu using appropriate codes.
• For Menu kinds of Programming , use the core logic of Loops/conditional statements.
• You need to strictly follow the syntaxes’s of that logic which you are using.
• Write the necessary comments for better understanding to you as well as to the faculty.

Adhere to the coding principles
-----------------------------------
Execution Flow of the Project:
----------------------------------
o First, display the food items available
o Then after the user can choose any of the item displayed
o Also take the quantity of selected food item by the customer, then ask the user that he/she wanna select more?
o If yes then again display the food items available and take an order from the customer. Here, you have to consider the total bill as the price of food items previously selected plus the price of new items added should display as a whole bill.
o If no then display the final bill on the screen */

#include <stdio.h>
int main()
{
  char choice;
  int qty;
  float CurrAmount = 0, TotalAmount = 0;
  char placeMoreOrder = 'y';

  while (placeMoreOrder == 'y' || placeMoreOrder == 'Y')
  {

    printf("Available Dishes in the Manu are: \n"
           "1. Pizza    price=180rs/pcs\n"
           "2. Burger   price=100rs/pcs\n"
           "3. Dosa     price=120rs/pcs\n"
           "4. Idli     price=50rs/pcs\n"
           "please Enter Your choice by entering 1,2,3 or 4:"

    );
    scanf(" %c", &choice);

    if (choice == '1')
    {
      printf("you have selected Pizza.");
      printf("Please Enter the Quantity.");
      scanf("%d", &qty);
      CurrAmount = (float)qty * 180;
      // printf("Amount is %f: ", CurrAmount);
    }
    else if (choice == '2')
    {
      printf("you have selected Burger.\n");
      printf("Please Enter the Quantity.\n");
      scanf("%d", &qty);
      CurrAmount = (float)qty * 100;
      // printf("Amount is %f:\t", CurrAmount);
    }
    else if (choice == '3')
    {
      printf("you have selected Dosa.\n");
      printf("Please Enter the Quantity.\n");
      scanf("%d", &qty);
      CurrAmount = (float)qty * 120;
      // printf("Amount is %f:\t", CurrAmount);
    }
    else if (choice == '4')
    {
      printf("you have selected Idli.\n");
      printf("Please Enter the Quantity.\n");
      scanf("%d", &qty);
      CurrAmount = (float)qty * 50;
      // printf("Amount is %f: \t", CurrAmount);
    }
    else
    {

      printf("you have Entered invalid input.\n");
      printf("Please Enter the valid choice.......\n");
      continue;
    }

    TotalAmount += CurrAmount;
    printf("Current Total: %f\n", TotalAmount);
    printf("Do you want to place more orders: Y/N \n");
    scanf(" %c", &placeMoreOrder);
    // if ((placeMoreOrder != 'y' || placeMoreOrder != 'Y') && (placeMoreOrder != 'n' || placeMoreOrder != 'N'))
    // {
    //   scanf("%c", &placeMoreOrder);
    // }
    // else
    // {
    //   printf("Enter Valid y/n:\n");

    // }
    // printf("Current Amount: %f\n", CurrAmount);
    // TotalAmount = CurrAmount + TotalAmount;
  }
  printf("Total Bill Amount is: %f\n", TotalAmount);
  printf("Thank you for your order please visit again..!!!!");

  return 0;
}