# `reduce()` function in Python, which is a higher-order function used to process iterables cumulatively. Here is the code for the examples shown in chronological order:

### 1. Basic Summation using `reduce()` (3:52)
# To sum all numbers in a list, you define a function that takes two arguments and pass it to `reduce()` along with your iterable.
from functools import reduce

def add(a, b):
    return a + b

nums = [10, 20, 30, 40]
result = reduce(add, nums)
print(result) # Output: 100


### 2. Using `lambda` Functions with `reduce()` (5:14)
# You can make the code more concise by replacing the standard function with a `lambda` expression.
from functools import reduce

nums = [10, 20, 30, 40]
result = reduce(lambda a, b: a + b, nums)
print(result)


### 3. Finding the Maximum Value (6:07)
# `reduce()` can also be used to compare elements and extract the largest value in a list by defining custom comparison logic.
from functools import reduce

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

nums = [10, 50, 30, 40]
result = reduce(find_max, nums)
print(result) # Output: 50
