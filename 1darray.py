"""CREATING dIFERENTES ARRAYS """

import numpy as np
"""if u want to check numpy version """
print("np.__version__")

"""INT ARRAY"""
x = np.arange(15)
print(x)

"""ARRAY WITH BOOLEANS"""
boolarray  = np.full((3,3), True, dtype = bool)
print(boolarray)

"""ARRAY WITH BOOLEANS POST RESHAPE"""
new_array = np.full(9, True, dtype = int).reshape(3,3)
print(new_array)

"""ARRAY WITH BOOLEANS"""
new_array2 = np.ones((3,3), dtype = bool)
print(new_array2)