"""STACKING ARRAYS VERTICALLY AND HORIZONTALLY"""

import numpy as np

a = np.arange(10).reshape(2,5)
b = np.repeat(1,10).reshape(2,-1)

"""VERTICAL STACKING"""
new_array = np.vstack([a,b])

"""HORIZONTAL STACKING"""
new_array2 = np.hstack([a,b])

print(new_array)
print(new_array2)