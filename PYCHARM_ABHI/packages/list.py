# using numpy check whether a list is empty or not
import numpy as np

my_list = [1,2,3] 

# Convert the list to a numpy array
arr = np.array(my_list)

# Check if the array is empty
if arr.size == 0:
    print("The list is empty")
else:
    print("The list is not empty")
