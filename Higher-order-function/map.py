# **map() function** in Python, a built-in higher-order function used to apply a specific operation to every item in an iterable.

### 1. Mapping Names to Lengths (3:01 - 7:59)
# The first example demonstrates how to convert a list of student names into a list containing the length of each name.
names = ['raj', 'यश', 'यशराज']

def find_length(name):
    return len(name)

mapped_obj = map(find_length, names)
print(list(mapped_obj)) # Output: [3, 4, 7]


### 2. Squaring Numbers (8:18 - 10:13)
# This section covers mapping a mathematical operation (squaring) over a list of integers.
nums = [5, 3, 8, 11, 6]

def square(n):
    return n * n

mapped_obj = map(square, nums)
print(list(mapped_obj)) # Output: [25, 9, 64, 121, 36]


### 3. Using Lambda Functions (10:14 - 10:55)
# Instead of defining a separate function, you can use a `lambda` function to write the mapping logic inline.
nums = [5, 3, 8, 11, 6]
mapped_obj = map(lambda n: n * n, nums)
print(list(mapped_obj))


### 4. Conditional Logic with Map (10:56 - 13:30)
# This demonstrates using `if-else` logic inside the mapped function to return different values based on whether a number is odd or even.
def process_num(n):
    if n % 2 != 0:
        return n * n       # Square if odd
    else:
        return n ** 3      # Cube if even

nums = [5, 3, 8, 11, 6]
print(list(map(process_num, nums))) 
# Output: [25, 9, 512, 121, 216]
