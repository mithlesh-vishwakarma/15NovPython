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
  int choice;
  printf("Available Dishes in the Manu are: \n"
         "1. Pizza    price=180rs/pcs\n"
         "2. Burger   price=100rs/pcs\n"
         "3. Dosa     price=120rs/pcs\n"
         "4. Idli     price=50rs/pcs\n"
         "please Enter Your choice by entering 1,2,3 or 4:  \t\t"

  );
  scanf("%d", &choice);
  switch (choice)
  {
  }
  return 0;
}