# Write a Python program to remove elements from a list using pop() and remove().

# Creating a list
my_list = ["Apple", "Banana", "Cherry", "Date", "Fig"]
print("Original list:", my_list)

# Removing elements using pop()
removed_item = my_list.pop(2)  # Remove element at index 2
print("\nAfter pop():", my_list)
print("Removed item:", removed_item)

removed_last = my_list.pop()  # Remove last element
print("\nAfter pop() (last element):", my_list)
print("Removed last item:", removed_last)

# Removing elements using remove()
my_list.remove("Banana")  # Remove specific value
print("\nAfter remove('Banana'):", my_list)

# Removing multiple elements using remove() in a loop
while "Date" in my_list:
    my_list.remove("Date")
print("After removing all 'Date':", my_list)