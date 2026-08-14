# Python's higher-order functions: `map()` and `filter()`. Below are the code examples.

### 1. Basic `map()` function 
# This example shows applying a logic function to a single list (marks) to increment each value by 1.
def logic(arg1):
    return arg1 + 1

marks = [60, 70, 80, 90, 100]
mapped_object = map(logic, marks)
print(list(mapped_object))


### 2. Using `map()` with multiple iterables
# The function can accept multiple iterables. Here, it adds elements from `marks`, `bonus`, and `bonus1` lists.
def logic(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

marks = [60, 70, 80, 90]
bonus = [1, 2, 3, 4]
bonus1 = [10, 20]

# Note: map stops at the shortest list
mapped_object = map(logic, marks, bonus, bonus1)
print(list(mapped_object))


### 3. Using `filter()` function 
# This example filters a dictionary of laptops based on a user-provided budget.
laptops = {'HP': 50000, 'Lenovo': 60000, 'Asus': 55000}
budget = float(input("Enter your budget: "))

def filter_items(item):
    # item corresponds to keys (e.g., 'HP')
    if laptops[item] <= budget:
        return True
    else:
        return False

filtered_object = filter(filter_items, laptops)
print(list(filtered_object))
