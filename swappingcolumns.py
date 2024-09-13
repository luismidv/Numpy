"""SWAP AND REVERSE COLUMNS/ROWS FROM A 2D NUMPY ARRAY"""

import numpy as np

array = np.arange(9).reshape(3,3)

"""SWAPPING COLUMNS"""
new_array = array[:,[1, 0, 2]]

"""SWAPPING ROWS"""
new_array2 = array[[1,0,2]]

"""REVERSE ROWS"""
new_array3 = array[::-1,:]

print("REVERSE COLUMNS")
new_array4 = array[:,::-1]

print("SWAP COLUMNS")
print(new_array)
print("SWAP ROWS")
print(new_array2)
print("REVERSE ROWS")
print(new_array3)
print("REVERSE COLUMNS")
print(new_array4)

