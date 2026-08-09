# Key Features of Tuples:
# 1)Immutability: Tuples cannot be changed in place, ensuring data integrity.
# 2)Performance: They are faster and more memory-efficient than lists.
# 3)Unpacking: Allows elegant assignment of tuple elements to variables.
# 4)Use as Keys: Can be used as dictionary keys or elements of sets.
# 5)Nested and Dynamic Operations: Support for nesting, slicing, and generator expressions.

# ** TUPLE OPERATIONS IN PYTHON **

# ** 1. Creating Tuples **
# Tuples are immutable sequences of elements.
empty_tuple = ()  # Empty tuple
single_element_tuple = (42,)  # Single element requires a trailing comma
mixed_tuple = (1, "hello", 3.14)  # Tuple with mixed types
nested_tuple = ((1, 2), (3, 4))  # Tuple containing other tuples
print("Tuples created:", empty_tuple, single_element_tuple, mixed_tuple, nested_tuple)

# ** 2. Accessing elements **
# Access using index (0-based indexing)
print("First element of mixed_tuple:", mixed_tuple[0])  # 1
print("Last element of mixed_tuple:", mixed_tuple[-1])  # 3.14

# Access nested tuple
print("Element in nested tuple:", nested_tuple[1][0])  # 3

# ** 3. Slicing Tuples **
# Extract a portion of the tuple (returns a new tuple)
sliced_tuple = mixed_tuple[1:]  # From index 1 to end
print("Sliced tuple:", sliced_tuple)

# ** 4. Immutability of Tuples **
# Tuples cannot be changed after creation
# mixed_tuple[0] = 100  # Uncommenting this line will raise a TypeError

# ** 5. Concatenating and repeating tuples **
# Using `+` to concatenate
concat_tuple = (1, 2) + (3, 4)
print("Concatenated tuple:", concat_tuple)

# Using `*` to repeat
repeated_tuple = ("A",) * 3
print("Repeated tuple:", repeated_tuple)

# ** 6. Checking membership **
# Using `in` and `not in`
is_in = 3.14 in mixed_tuple  # True
is_not_in = "world" not in mixed_tuple  # True
print("Membership check:", is_in, is_not_in)

# ** 7. Tuple unpacking **
# Assigning tuple elements to variables
a, b, c = (10, 20, 30)
print("Unpacked values:", a, b, c)

# Unpacking with `*` for variable-length unpacking
first, *rest = (1, 2, 3, 4)
print("Unpacked with *:", first, rest)

# ** 8. Looping through tuples **
# Using a `for` loop
for element in mixed_tuple:
    print("Tuple element:", element)

# Using `enumerate()` to get index and value
for index, value in enumerate(mixed_tuple):
    print(f"Index {index}: Value {value}")

# ** 9. Tuple methods **
# Count occurrences of an element
count_of_hello = mixed_tuple.count("hello")  # 1
print("Count of 'hello':", count_of_hello)

# Find the index of an element
index_of_hello = mixed_tuple.index("hello")  # 1
print("Index of 'hello':", index_of_hello)

# ** 10. Converting to and from tuples **
# Converting a list to a tuple
sample_list = [1, 2, 3]
list_to_tuple = tuple(sample_list)
print("Converted list to tuple:", list_to_tuple)

# Converting a tuple to a list
tuple_to_list = list(mixed_tuple)
print("Converted tuple to list:", tuple_to_list)

# ** 11. Immutable nature workaround: Creating a new tuple **
# To "modify" a tuple, create a new one
modified_tuple = mixed_tuple[:1] + ("world",) + mixed_tuple[2:]
print("Modified tuple:", modified_tuple)

# ** 12. Nested Tuples and accessing them **
nested = (("a", "b"), (1, 2, 3), ("x", "y", "z"))
print("Accessing nested element:", nested[1][2])  # 3

# ** 13. Using tuples as dictionary keys **
# Tuples can be used as keys in dictionaries because they are immutable
tuple_key_dict = {("key1", "key2"): "value", (1, 2): "numbers"}
print("Dictionary with tuple keys:", tuple_key_dict)
print("Accessing value by tuple key:", tuple_key_dict[("key1", "key2")])

# ** 14. Sorting tuples **
# Sorting a tuple requires converting it to a list
unsorted_tuple = (3, 1, 4, 2)
sorted_tuple = tuple(sorted(unsorted_tuple))
print("Sorted tuple:", sorted_tuple)

# ** 15. Tuple comprehension (Generator Expression) **
# Tuples don't have comprehensions, but generator expressions can be used
squared_values = tuple(x**2 for x in range(5))
print("Generated tuple with squares:", squared_values)

# ** 16. Checking length of a tuple **
print("Length of mixed_tuple:", len(mixed_tuple))

# ** 17. Minimum and maximum values in a tuple **
numeric_tuple = (10, 20, 5, 30)
print("Minimum value in numeric_tuple:", min(numeric_tuple))
print("Maximum value in numeric_tuple:", max(numeric_tuple))

# ** 18. Packing and unpacking tuples dynamically **
# Packing: Creating a tuple from multiple values
packed_tuple = 1, 2, 3  # Equivalent to (1, 2, 3)
print("Packed tuple:", packed_tuple)

# Unpacking with varying number of variables
x, y, *z = packed_tuple + (4, 5)
print("Dynamic unpacking:", x, y, z)

# ** 19. Using `zip()` with tuples **
# Zipping multiple sequences together
names = ("Alice", "Bob", "Charlie")
scores = (85, 90, 95)
zipped = tuple(zip(names, scores))
print("Zipped tuples:", zipped)

# ** 20. Nested operations with tuples **
# Applying a function to all elements using `map`
squared = tuple(map(lambda x: x**2, numeric_tuple))
print("Squared numeric_tuple:", squared)

# ** 21. Memory efficiency of tuples **
# Tuples use less memory than lists
import sys
print("Memory size of tuple:", sys.getsizeof(mixed_tuple), "bytes")
print("Memory size of equivalent list:", sys.getsizeof(list(mixed_tuple)), "bytes")

# Summary of tuples:
# - Immutable: Cannot be changed after creation.
# - Memory efficient: Use less memory compared to lists.
# - Useful for fixed collections and as dictionary keys.
