# Q. Write a Python program that demonstrates the correct use of indentation, comments, and variables following PEP 8 guidelines.


# This program calculates total price
# and applies discount if applicable.

# variables
price_per_item = 250
quantity = 5

# calculate total price
total_price = price_per_item * quantity

# discount rate
discount_rate = 0.10  # 10% discount

# apply discount if total is greater than 1000
if total_price > 1000:
    discount = total_price * discount_rate
    final_price = total_price - discount
else:
    final_price = total_price

# output results
print("Price per item:", price_per_item)
print("Quantity:", quantity)
print("Total price:", total_price)
print("Final price after discount:", final_price)


# -------------------------------------------------------------------------------------


# """
# ==================== PEP 8 GUIDELINES ====================

# 1. VARIABLES (Naming Rules)
# ----------------------------------------------------------
# - Use lowercase letters with underscores (snake_case)
#     ✔ total_price
#     ✔ user_name
#     ✔ item_count

# - Avoid camelCase and PascalCase for variables
#     ✘ totalPrice
#     ✘ TotalPrice

# - Use meaningful and descriptive names
#     ✔ total_price  (good)
#     ✘ tp           (bad)

# - Constants should be in uppercase
#     ✔ MAX_LIMIT = 100

# ----------------------------------------------------------

# 2. INDENTATION
# ----------------------------------------------------------
# - Use 4 spaces for each indentation level (NOT tabs)

# - Keep consistent indentation throughout the code

# Correct:
#     if price > 1000:
#         print("High price")

# Wrong:
#     if price > 1000:
#       print("Bad indentation")

# - Avoid mixing tabs and spaces

# ----------------------------------------------------------

# 3. COMMENTS
# ----------------------------------------------------------
# - Use comments to explain WHY, not obvious WHAT

# - Single-line comments start with #
#     # This is a comment

# - Add a space after #
#     ✔ # Good comment
#     ✘ #Bad comment

# - Inline comments should have at least 2 spaces before #
#     total = price * qty  # calculate total price

# - Use clear and simple language

# ----------------------------------------------------------

# 4. DOCSTRINGS (for functions/classes)
# ----------------------------------------------------------
# - Use triple double quotes """

# - Describe what the function does

# Example:
#     def calculate_total(price, qty):
#         """Return total price."""
#         return price * qty

# ----------------------------------------------------------

# 5. GENERAL CLEAN CODE RULES
# ----------------------------------------------------------
# - Keep line length under 79 characters (recommended)

# - Add blank lines:
#     - 2 blank lines before function definitions
#     - 1 blank line inside functions if needed

# - Avoid unnecessary spaces:
#     ✔ total = price * qty
#     ✘ total=price*qty

# ==========================================================
# """
