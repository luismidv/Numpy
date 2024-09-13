"""EXTRACT NUMBERS ON A GIVEN RANGE FROM A NUMPY ARRAY"""

import numpy as np

array = np.arange(10)

"""DO NOT USE and INSTEAD OF & DOESN'T WORK"""
new_array = array[(array >= 5) & (array<=10)]
print(new_array)
