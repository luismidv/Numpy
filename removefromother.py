"""REMOVE ITEMS OF AN ARRAY THAT EXISTS ON OTHER ARRAY"""

import numpy as np

a = np.arange(10)
b = np.arange(5,15)

new_array = np.setdiff1d(a,b)
print(new_array)