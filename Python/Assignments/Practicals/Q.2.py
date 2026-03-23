# Q. Write a Python program that demonstrates the correct use of indentation, comments, and variablesfollowing PEP 8 guidelines.

"""
This program calculates the total price of items
and applies a discount if applicable.
"""


def calculate_total_price(price_per_item, quantity):
    """
    Calculate total price based on price per item and quantity.
    """
    total_price = price_per_item * quantity
    return total_price


def apply_discount(total_price):
    """
    Apply a 10% discount if total price is greater than 1000.
    """
    discount_rate = 0.10  # 10% discount

    if total_price > 1000:
        discount = total_price * discount_rate
        final_price = total_price - discount
    else:
        final_price = total_price

    return final_price


def main():
    """
    Main function to run the program.
    """
    # Variables for item price and quantity
    price_per_item = 250
    quantity = 5

    # Calculate total price
    total_price = calculate_total_price(price_per_item, quantity)

    # Apply discount if eligible
    final_price = apply_discount(total_price)

    # Display results
    print("Price per item:", price_per_item)
    print("Quantity:", quantity)
    print("Total price:", total_price)
    print("Final price after discount:", final_price)


# Entry point of the program
if __name__ == "__main__":
    main()
