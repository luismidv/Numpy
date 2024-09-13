"""FIND COMMON ITEMS BETWEEN NUMPY ARRAYS"""

import numpy as np

a = np.arange(10)
b = np.arange(5,15)

print(a)
print(b)

new_array = np.intersect1d(a,b)
print(new_array)