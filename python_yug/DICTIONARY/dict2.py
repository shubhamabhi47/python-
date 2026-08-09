# a dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value. Dictionaries are unordered,
# which means that the order of the elements is not guaranteed. 
# They are commonly used to store and retrieve data efficiently, especially when you need fast lookups based on keys.

# dict1 = {"name": "John", "age": 30}
# dict2 = {"city": "New York", "country": "USA"}
# dict1.update(dict2)
# print(dict1)

my_dict = {1 : "Shubham", 2 : "Abhimanyu" }
for key in my_dict:
    value = my_dict[key]
    print(f"{key}: {value}")
    
    
for key, value in my_dict.items():
    print(f"{key}: {value}")
    

    


my_dict = {"apple": 2, "banana": 4, "orange": 6}
print(my_dict.keys())  # Output: dict_keys(['apple', 'banana', 'orange'])
print(my_dict.values())  # Output: dict_values([2, 4, 6])
print(my_dict.items())  # Output: dict_items([('apple', 2), ('banana', 4), ('orange', 6)])
print(my_dict.get("apple"))  # Output: 2
print(my_dict.get("grape"))  # Output: None
print(my_dict.get("grape", 0))  # Output: 0


my_dict = {"apple": 2, "banana": 4, "orange": 6}
print(my_dict.pop("banana"))  # Output: 4
print(my_dict)  # Output: {"apple": 2, "orange": 6}
print(my_dict.pop("grape", 0))  # Output: 0