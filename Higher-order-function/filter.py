#  **filter() function** in Python, which is a built-in higher-order function used to extract elements from an iterable based on a specific condition.

### 1. Introduction to Higher-Order Functions (0:00 - 1:04)
# **Theory:** A higher-order function is a function that takes another function as an argument or returns one. Python provides three core built-in higher-order functions: `filter()`, `map()`, and `reduce()`.

### 2. Purpose and Syntax of `filter()` (1:06 - 3:48)
# **Theory:** The `filter()` function is used for data filtration. It evaluates each element in an iterable against a function (the logic) and returns only those elements for which the function returns `True`.
# * **Syntax:** `filter(function_name, iterable)`
# * **Arguments:** 
#     1. **function_name:** The logic/test to apply to each element.
#     2. **iterable:** The collection (list, tuple, etc.) to be filtered.

### 3. Basic Example: Filtering Even Numbers (3:49 - 9:58)
# **Theory:** You define a function that tests for a condition. If the condition is met, the function returns `True` (keeping the element); otherwise, it returns `False` (removing it).

# Data to filter
data = [23, 22, 36, 54, 59, 90]

# Logic function
def is_even(num):
    return num % 2 == 0

# Using filter()
filtered_obj = filter(is_even, data)

# Converting to list to view result
print(list(filtered_obj))  # Output: [22, 36, 54, 90]

# we can use loop too but we can not print directly filtered_object like print(filtered_object) it gives memory location
for ele in filtered_obj:
    print(ele)

### 4. Working Mechanism and Memory (9:59 - 13:00)
# **Theory:** `filter()` returns a **filter object** (an iterator). Once you consume it (e.g., convert to a `list` or iterate with a `for` loop), it becomes exhausted and empty. If no value is explicitly returned in your logic function, Python treats it as `None` (which evaluates to `False`), effectively filtering the element out.

### 5. Using Lambda Expressions (16:06 - 18:16)
# **Theory:** In real-world projects, developers often use `lambda` functions instead of full function definitions for conciseness when the logic is simple.

# Using lambda with filter
data = [23, 22, 36, 54, 59, 90]

# Direct filtering for even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, data))
print(even_numbers) # [22, 36, 54, 90]

# Filtering for odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, data))
print(odd_numbers) # [23, 59]
