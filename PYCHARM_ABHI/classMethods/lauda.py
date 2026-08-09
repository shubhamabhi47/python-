import numpy as np
# Step 1: Create a 1D array with values from 0 to 47
arr_1d = np.arange(12)

# Step 2: Reshape the array into a 4D array with shape (2, 3, 2, 4)
arr_4d = arr_1d.reshape(2, 3, 2)
print(arr_4d)
