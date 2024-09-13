"""RESHAPING ARRAYS"""

import numpy as np

array = np.arange(10)
print(array)

new_array = array.reshape(2,5)
print(new_array)

"""WHEN YOU USE -1 THIS WILL AUTOMATICALLY DECIDE THE NUMBERS OF COLUMNS/ROWS """
new_array1 = array.reshape(2,-1)
print(new_array1)
