# A dictionary allows you to use anything, not just numbers. A dictionary connects one item to another.

# Dictionary is a collection of Key-value pairs. They are indexed with the help of keys.

# you can use nearly anything to obtain the data. 
# This allows you to use a dict as a database for storing and organizing data.
# you can only retrieve things from a list using numbers(integers).

#  Lists and Tuples are some of the other data types.
# Dictionaries are indexed by keys and can be of any immutable type. These are unordered key-value pairs with unique keys.



# Creating a dictionary using curly braces
my_dict = {"apple": 2, "banana": 4, "orange": 6}

# Creating a dictionary using the dict() function
my_dict = dict(apple=2, banana=4, orange=6)

# add elements to dictionary
my_info = {
    "Name": "Abhii",
    "Age": 20,
    "Gender": "Male",
    "Location": "India",
    "Website": "anything.com"
}

# print dictionary
print(my_info)
# print value of a key
print(my_info['Name'])
# modify elements in dictionary
my_info['Age'] = 24
print(my_info)
# length of dictionary
print(len(my_info))
# delete a particular key
del my_info['Website']
print(my_info)
# removes all elements in dictionary
my_info.clear()
print(my_info)
# delete entire dictionary
# del my_info
