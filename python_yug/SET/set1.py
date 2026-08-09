# Creating sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"set1: {set1}, set2: {set2}")
# Output: set1: {1, 2, 3}, set2: {3, 4, 5}

# Adding an element
set1.add(6)
print(f"After adding 6 to set1: {set1}")
# Output: After adding 6 to set1: {1, 2, 3, 6}

# Removing an element
set1.remove(2)
print(f"After removing 2 from set1: {set1}")
# Output: After removing 2 from set1: {1, 3, 6}

# Discarding an element (no error if element doesn't exist)
set1.discard(10)  # 10 does not exist
print(f"After discarding 10 from set1: {set1}")
# Output: After discarding 10 from set1: {1, 3, 6}

# Union
union_set = set1.union(set2)
print(f"Union of set1 and set2: {union_set}")
# Output: Union of set1 and set2: {1, 3, 4, 5, 6}

# Intersection
intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_set}")
# Output: Intersection of set1 and set2: {3}

# Difference
difference_set = set1.difference(set2)
print(f"Difference of set1 and set2 (set1 - set2): {difference_set}")
# Output: Difference of set1 and set2 (set1 - set2): {1, 6}

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print(f"Symmetric Difference of set1 and set2: {symmetric_difference_set}")
# Output: Symmetric Difference of set1 and set2: {1, 4, 5, 6}

# Subset and Superset Checks
set3 = {1, 3}
print(f"set3: {set3}")
# Output: set3: {1, 3}
print(f"set3 is subset of set1: {set3.issubset(set1)}")
# Output: set3 is subset of set1: True
print(f"set1 is superset of set3: {set1.issuperset(set3)}")
# Output: set1 is superset of set3: True

# Pop a random element
popped_element = set1.pop()
print(f"After popping an element from set1: Popped element: {popped_element}, set1: {set1}")
# Output: After popping an element from set1: Popped element: 1, set1: {3, 6}

# Clearing the set
set1.clear()
print(f"After clearing set1: {set1}")
# Output: After clearing set1: set()
