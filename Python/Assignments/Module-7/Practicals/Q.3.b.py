# Write a Python program to sort a list using both sort() and sorted().

# Creating a list
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original list:", my_list)

# Sorting using sort() method (in-place)
my_list.sort()
print("\nAfter sort():", my_list)

# Sorting in reverse order
my_list.sort(reverse=True)
print("After sort(reverse=True):", my_list)

# Creating a new sorted list using sorted() function
original_list = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_list = sorted(original_list)
print("\nOriginal list:", original_list)
print("Using sorted():", sorted_list)

# Sorting with custom key
my_list = ["Apple", "Banana", "Cherry", "Date"]
sorted_by_length = sorted(my_list, key=len)
print("\nSorted by length:", sorted_by_length)