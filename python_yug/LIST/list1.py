# my_list = [1, 2, 3, 4, 5]
# print(my_list[2]) # Output: 3


# my_list = [10, 20, 30, 40, 50]
# target = 30
# for element in my_list:
#     if (element == target):
#         print("Element found!")
#         break
#     else:
#         print("Element not found.")
        
        
# my_list = [10, 20, 30, 40, 50]
# target = 30
# for index, element in enumerate(my_list):  # Use enumerate to track indices
#     if element == target:
#         print("Element found! at index", index)
#         break
# else:
#     print("Element not found.")  # Executed only if the loop completes without `break`




# a = [2, 3, 5, 7, 9]
# k = 5

# for i in range(len(a)):
#     if a[i] == k:
#         print('Found element at index:', i)
#         break
#     else:
#         print('Not found')
        


a = [2, 3, 5, 7, 9]
k = 10  # Value to check
found = False
for index, value in enumerate(a):
    if value == k:
        print(True)
        print(f"Index: {index}, Value: {value}")
        found = True
        break
if not found:
    print(False)