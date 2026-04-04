# Write a Python program to concatenate two tuples.

# Creating two tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

# Concatenating tuples
concatenated_tuple = tuple1 + tuple2
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Concatenated tuple:", concatenated_tuple)

# Concatenating with different data types
tuple3 = (10, 20)
tuple4 = ("Hello", 3.14, True)
concatenated_tuple2 = tuple3 + tuple4
print("\nTuple 3:", tuple3)
print("Tuple 4:", tuple4)
print("Concatenated tuple:", concatenated_tuple2)

# Concatenating with repetition
tuple5 = (1, 2)
repeated_tuple = tuple5 * 3
print("\nTuple 5:", tuple5)
print("Repeated tuple:", repeated_tuple)