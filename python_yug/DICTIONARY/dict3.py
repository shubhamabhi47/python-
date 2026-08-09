person = {
  "name": "Abhii",
  "age": 20,
  "contact": {
    "email": "ebhii@example.com",
    "phone": "123-456-7890"
  }
}

squares = {x: x**2 for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary example
person = {
    "name": "Abhii",  # String value
    "age": 20,        # Integer value
    "contact": {      # Nested dictionary
        "email": "ebhii@example.com",
        "phone": "123-456-7890"
    }
}

# ** 1. Accessing values using keys **
# Accessing dictionary values
print("Name:", person["name"])  # Output: Name: Abhii
print("Email:", person["contact"]["email"])  # Accessing nested dictionary

# Using the `get()` method for safe access (avoids KeyError if key doesn't exist)
print("Nickname:", person.get("nickname", "Not provided"))  # Default value

# ** 2. Adding and updating key-value pairs **
# Adding a new key-value pair
person["nickname"] = "Abhi"
print("After adding nickname:", person)

# Updating an existing key's value
person["age"] = 21  # Updates the value of 'age'
print("After updating age:", person)

# If the same key is added again, it overwrites the previous value
person["name"] = "Abhinav"
print("After modifying name (duplicate key handling):", person)
# Explanation: A dictionary does not allow duplicate keys. The last value assigned to a key is retained.

# ** 3. Removing key-value pairs **
# Using `pop()` to remove a key-value pair (returns the value removed)
removed_value = person.pop("nickname", None)
print("Removed nickname value:", removed_value)
print("After removing nickname:", person)

# Using `del` keyword to delete a key-value pair
del person["contact"]
print("After deleting contact:", person)

# Using `clear()` to remove all items
person_copy = person.copy()  # Creating a copy to demonstrate
person_copy.clear()
print("After clearing the dictionary:", person_copy)

# ** 4. Iterating through a dictionary **
# Iterating through keys
print("Keys:")
for key in person:
    print(key)

# Iterating through values
print("Values:")
for value in person.values():
    print(value)

# Iterating through key-value pairs
print("Key-Value Pairs:")
for key, value in person.items():
    print(f"{key}: {value}")

# ** 5. Checking if a key exists **
if "name" in person:
    print("'name' key exists in the dictionary")

# ** 6. Merging dictionaries **
new_data = {"city": "Delhi", "hobby": "Painting"}
# Using `update()` to merge dictionaries
person.update(new_data)
print("After merging with new_data:", person)

# ** 7. Dictionary comprehension **
# Creating a new dictionary by modifying existing one
squared_numbers = {x: x**2 for x in range(1, 6)}  # Keys and values are squares
print("Dictionary comprehension result:", squared_numbers)

# ** 8. Deep copying vs shallow copying **
import copy
# Shallow copy (references nested dictionary)
shallow_copy = person.copy()
shallow_copy["name"] = "Changed"
print("Shallow Copy:", shallow_copy)
print("Original Dictionary (unchanged):", person)

# Deep copy (creates a full independent copy)
deep_copy = copy.deepcopy(person)
deep_copy["name"] = "Deep Copy"
print("Deep Copy:", deep_copy)
print("Original Dictionary after deep copy:", person)

# ** 9. Length of a dictionary **
print("Length of person dictionary:", len(person))

# ** 10. Sorting a dictionary (keys) **
sorted_dict = dict(sorted(person.items()))  # Sorting based on keys
print("Sorted dictionary:", sorted_dict)

# ** 11. Nesting and accessing nested values **
person["contact"] = {  # Adding contact back for nesting demonstration
    "email": "ebhii@example.com",
    "phone": "123-456-7890"
}
print("Accessing nested value (email):", person["contact"]["email"])

# Summary of functionality:
# - Dictionaries are unordered (in Python 3.7+, they maintain insertion order).
# - Keys must be unique; duplicates overwrite previous values.
# - They are mutable, allowing modifications and updates.
# - Useful for structured data due to nesting capabilities.

# ** 12. Default value for keys using defaultdict **
from collections import defaultdict

# defaultdict automatically initializes keys with a default value
default_dict = defaultdict(int)  # Default value is 0 for integers
default_dict["a"] += 1
default_dict["b"] += 2
print("defaultdict example:", default_dict)

# ** 13. Setting default values using `setdefault()` **
# Adds a key with a default value if the key doesn't exist
person.setdefault("profession", "Student")
print("After setdefault (adding profession):", person)
# If key exists, does nothing
person.setdefault("age", 30)
print("After setdefault (existing key 'age'):", person)

# ** 14. Removing an arbitrary item using `popitem()` **
# Removes and returns the last inserted key-value pair
last_item = person.popitem()
print("Last item removed:", last_item)
print("After popitem:", person)

# ** 15. Dictionary views: keys, values, and items (dynamic views) **
# Keys view
keys_view = person.keys()
print("Keys view (before modification):", list(keys_view))
# Values view
values_view = person.values()
print("Values view (before modification):", list(values_view))
# Items view
items_view = person.items()
print("Items view (before modification):", list(items_view))

# Modifying the dictionary affects the views dynamically
person["hobby"] = "Music"
print("Keys view (after modification):", list(keys_view))
print("Values view (after modification):", list(values_view))
print("Items view (after modification):", list(items_view))

# ** 16. Using a dictionary as a counter **
# Counting occurrences of elements
from collections import Counter
sample_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
count_dict = Counter(sample_list)
print("Counter example:", count_dict)

# ** 17. Checking equality of dictionaries **
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 3, "b": 2, "a": 1}  # Same keys/values, different order
print("Are dict1 and dict2 equal?", dict1 == dict2)

# ** 18. Dictionary unpacking (merging dictionaries using `**`) **
dict3 = {"x": 100, "y": 200}
merged_dict = {**dict1, **dict3}  # Merges dict1 and dict3
print("Merged dictionary using `**`:", merged_dict)

# ** 19. Filtering a dictionary using comprehension **
# Keeping only items where value > 1
filtered_dict = {key: value for key, value in count_dict.items() if value > 1}
print("Filtered dictionary (values > 1):", filtered_dict)

# ** 20. Inverting a dictionary (keys become values and vice versa) **
original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {value: key for key, value in original_dict.items()}
print("Inverted dictionary:", inverted_dict)

# ** 21. Accessing nested dictionaries safely **
# Using `get` with nested dictionaries
nested_value = person.get("contact", {}).get("phone", "Not available")
print("Accessing nested value safely:", nested_value)

# ** 22. Using `zip()` to create a dictionary from two lists **
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
zipped_dict = dict(zip(keys, values))
print("Dictionary created with zip:", zipped_dict)

# ** 23. Sorting a dictionary by values **
# Sorting by values (ascending order)
sorted_by_values = dict(sorted(original_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by values (ascending):", sorted_by_values)

# Sorting by values (descending order)
sorted_by_values_desc = dict(sorted(original_dict.items(), key=lambda item: item[1], reverse=True))
print("Dictionary sorted by values (descending):", sorted_by_values_desc)

# ** 24. Copying dictionaries with `copy()` and `deepcopy()` **
# Shallow copy
shallow_copy = person.copy()
shallow_copy["age"] = 99
print("Shallow copy modified:", shallow_copy)
print("Original dictionary after shallow copy:", person)

# Deep copy
from copy import deepcopy
deep_copy = deepcopy(person)
deep_copy["contact"] = {"email": "new@example.com"}
print("Deep copy modified:", deep_copy)
print("Original dictionary after deep copy:", person)

# ** 25. Counting keys and values separately **
key_count = len(person.keys())
value_count = len(person.values())
print(f"Number of keys: {key_count}, Number of values: {value_count}")

# ** 26. Using `dict.fromkeys()` to create a dictionary with default values **
default_value_dict = dict.fromkeys(["key1", "key2", "key3"], "default_value")
print("Dictionary with default values:", default_value_dict)

# ** 27. Combining dictionaries using `collections.ChainMap` **
from collections import ChainMap
dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}
combined = ChainMap(dict_a, dict_b)
print("Combined dictionaries using ChainMap:", combined)
# Access keys in the combined dictionary
print("Value of 'a':", combined["a"])
print("Value of 'c':", combined["c"])

# ** 28. Modifying dictionary keys dynamically (e.g., renaming) **
renamed_keys = {("prefix_" + key): value for key, value in original_dict.items()}
print("Dictionary with renamed keys:", renamed_keys)

# ** 29. Check dictionary's memory usage using sys module **
import sys
print("Memory size of dictionary:", sys.getsizeof(person), "bytes")

