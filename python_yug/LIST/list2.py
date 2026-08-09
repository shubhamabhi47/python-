# a = list(range(10))
# print(a)        # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[::-2])


# Using a tuple
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)

# Using a string
my_string = "Hello, World!"
my_list = list(my_string)



li = [2, 23, 49, 6, 71, 55]
print("Reveersing a list:",li[::-1])  # Output: [55, 71, 6, 49, 23, 2]

print("Slicing a list")
li = [2, 3, 4, 5, 6]
n = 2
print("Rotation of list to given index:",li[n:] + li[:n])  # Output: [4, 5, 6, 2, 3]

