# ** TUPLE OPERATIONS IN PYTHON **

# ** Basic Operations **

# ** 1. Creating Tuples **
empty_tuple = ()  # Empty tuple
single_element_tuple = (42,)  # Single element tuple (requires a trailing comma)
simple_tuple = (1, 2, 3)  # Tuple with integers
mixed_tuple = (1, "hello", 3.14)  # Tuple with mixed types
nested_tuple = ((1, 2), (3, 4))  # Tuple containing other tuples
print("Basic Tuples:", empty_tuple, single_element_tuple, simple_tuple, mixed_tuple, nested_tuple)
# Output: Basic Tuples: () (42,) (1, 2, 3) (1, 'hello', 3.14) ((1, 2), (3, 4))

# ** 2. Accessing Elements **
print("First element of simple_tuple:", simple_tuple[0])  # Output: First element of simple_tuple: 1
print("Last element of mixed_tuple:", mixed_tuple[-1])  # Output: Last element of mixed_tuple: 3.14
print("Nested tuple element:", nested_tuple[1][0])  # Output: Nested tuple element: 3

# ** 3. Slicing Tuples **
sliced_tuple = simple_tuple[1:]  # From index 1 to the end
print("Sliced tuple:", sliced_tuple)  # Output: Sliced tuple: (2, 3)

# ** 4. Immutability of Tuples **
# Tuples cannot be modified after creation
# simple_tuple[0] = 100  # Uncommenting this line will raise a TypeError

# ** 5. Tuple Concatenation and Repetition **
concat_tuple = (1, 2) + (3, 4)
print("Concatenated tuple:", concat_tuple)  # Output: Concatenated tuple: (1, 2, 3, 4)
repeated_tuple = ("A",) * 3
print("Repeated tuple:", repeated_tuple)  # Output: Repeated tuple: ('A', 'A', 'A')

# ** 6. Membership Testing **
is_in = 2 in simple_tuple  # True
is_not_in = "world" not in mixed_tuple  # True
print("Membership check:", is_in, is_not_in)  # Output: Membership check: True True

# ** 7. Length of Tuple **
print("Length of mixed_tuple:", len(mixed_tuple))  # Output: Length of mixed_tuple: 3

# ** 8. Iterating Through Tuples **
for element in mixed_tuple:
    print("Element in mixed_tuple:", element)
# Output:
# Element in mixed_tuple: 1
# Element in mixed_tuple: hello
# Element in mixed_tuple: 3.14

for index, value in enumerate(simple_tuple):
    print(f"Index {index}: Value {value}")
# Output:
# Index 0: Value 1
# Index 1: Value 2
# Index 2: Value 3

# ** 9. Tuple Methods **
count_hello = mixed_tuple.count("hello")  # 1
print("Count of 'hello':", count_hello)  # Output: Count of 'hello': 1
index_hello = mixed_tuple.index("hello")  # 1
print("Index of 'hello':", index_hello)  # Output: Index of 'hello': 1

# ** Intermediate Operations **

# ** 10. Tuple Unpacking **
a, b, c = simple_tuple
print("Unpacked values:", a, b, c)  # Output: Unpacked values: 1 2 3

first, *rest = (1, 2, 3, 4)
print("Unpacking with *:", first, rest)  # Output: Unpacking with *: 1 [2, 3, 4]

# ** 11. Converting to and from Tuples **
sample_list = [10, 20, 30]
list_to_tuple = tuple(sample_list)
print("List to tuple:", list_to_tuple)  # Output: List to tuple: (10, 20, 30)
tuple_to_list = list(simple_tuple)
print("Tuple to list:", tuple_to_list)  # Output: Tuple to list: [1, 2, 3]

# ** 12. Modifying Tuples by Recreating **
modified_tuple = simple_tuple[:1] + (100,) + simple_tuple[2:]
print("Modified tuple:", modified_tuple)  # Output: Modified tuple: (1, 100, 3)

# ** 13. Using Tuples as Dictionary Keys **
tuple_key_dict = {("key1", "key2"): "value", (1, 2): "numbers"}
print("Dictionary with tuple keys:", tuple_key_dict)  # Output: Dictionary with tuple keys: {('key1', 'key2'): 'value', (1, 2): 'numbers'}
print("Value for ('key1', 'key2'):", tuple_key_dict[("key1", "key2")])
# Output: Value for ('key1', 'key2'): value

# ** Advanced Operations **

# ** 14. Sorting Tuples **
unsorted_tuple = (3, 1, 4, 2)
sorted_tuple = tuple(sorted(unsorted_tuple))
print("Sorted tuple:", sorted_tuple)  # Output: Sorted tuple: (1, 2, 3, 4)

# ** 15. Tuple Comprehension (Using Generators) **
squared_values = tuple(x**2 for x in range(5))
print("Generated tuple with squares:", squared_values)  # Output: Generated tuple with squares: (0, 1, 4, 9, 16)

# ** 16. Packing and Unpacking Dynamically **
packed_tuple = 1, 2, 3  # Equivalent to (1, 2, 3)
print("Packed tuple:", packed_tuple)  # Output: Packed tuple: (1, 2, 3)
x, y, *z = packed_tuple + (4, 5)
print("Unpacked dynamically:", x, y, z)  # Output: Unpacked dynamically: 1 2 [3, 4, 5]

# ** 17. Using `zip()` with Tuples **
names = ("Alice", "Bob", "Charlie")
scores = (85, 90, 95)
zipped = tuple(zip(names, scores))
print("Zipped tuples:", zipped)  # Output: Zipped tuples: (('Alice', 85), ('Bob', 90), ('Charlie', 95))

# ** 18. Nested Tuples and Accessing Them **
nested = ((1, 2), (3, 4), (5, (6, 7)))
print("Nested tuple element:", nested[2][1][0])  # Output: Nested tuple element: 6

# ** 19. Applying Functions to Tuples **
numeric_tuple = (10, 20, 30)
squared_tuple = tuple(map(lambda x: x**2, numeric_tuple))
print("Squared tuple:", squared_tuple)  # Output: Squared tuple: (100, 400, 900)

# ** 20. Memory Efficiency of Tuples **
import sys
tuple_memory = sys.getsizeof(simple_tuple)
list_memory = sys.getsizeof(list(simple_tuple))
print("Memory used by tuple:", tuple_memory, "bytes")  # Output: Memory used by tuple: 64 bytes (depends on system)
print("Memory used by equivalent list:", list_memory, "bytes")  # Output: Memory used by equivalent list: 88 bytes (depends on system)



# Summary of Tuples:
# - Tuples are immutable and fixed in size.
# - Ideal for fixed collections of items.
# - They are faster and memory-efficient compared to lists.
# - Useful as dictionary keys or elements of sets.
