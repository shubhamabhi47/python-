# append(value): Adds an element to the end of the list.
# insert(index , value): Inserts an element at a specific index.
# remove(value): Removes the first occurrence of a specific value.
# pop(index): Removes and returns an element by index.
# pop(without index): Removes and returns an element by index.
# extend(list): Appends the contents of another list.
# count(): Returns the number of occurrences of a value.
# index(): Returns the index of the first occurrence of a value.
# sort(): Sorts the list in ascending order.
# reverse(): Reverses the order of elements.
# copy(): Creates a shallow copy of the list.
# clear(): Removes all elements from the list.
# del: Removes all elements from the list.


print("1.Insertion or deletion at the end of the list: O(1)")
my_list = [1, 2, 3]
my_list.append(4) # [1, 2, 3, 4]
my_list.pop() # [1, 2, 3]


# When inserting or deleting an element at the beginning or middle of a Python list, 
# the remaining elements must be shifted to accommodate the change. As a result, 
# these operations have a linear time complexity of O(n). 
# The time taken depends on the number of elements that need to be shifted
print("2.Insertion or deletion at the beginning or middle of the list: O(n)")
my_list = [1, 2, 3]
my_list.insert(0, 0) # [0, 1, 2, 3]
my_list.pop(2) # [0, 1, 3]


# Inserting or deleting an element at a specific index in a Python list requires shifting elements to accommodate the change. As a result, 
# these operations have a linear time complexity of O(n). 
# The time taken depends on the number of elements that need to be shifted.
print("3.Insertion or deletion at a specific index: O(n))")
my_list = [1, 2, 3, 4]
my_list.insert(2, 2.5) # [1, 2, 2.5, 3, 4]
my_list.pop(1) # [1, 2.5, 3, 4]


print("4.Appending one list to another: O(k)")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 += list2 # [1, 2, 3, 4, 5, 6]

print("5.Extending one list with another: O(k)")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2) 
print(list1)# [1, 2, 3, 4, 5, 6]



print("6.Slicing a list: O(k)")
my_list = [1, 2, 3, 4, 5]
sublist = my_list[1:4] # [2, 3, 4]


print("Reversing list:")
my_list = [10, 20, 30, 40, 50]
my_list.reverse()


print("Sorting a list")
my_list = [50, 10, 40, 20, 30]
my_list.sort()


print("Copying a list")
original_list = [1, 2, 3]
shallow_copy = original_list.copy()