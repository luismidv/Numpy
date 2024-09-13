"""GENERATE CUSTOM NUMBER SECUENCES"""

import numpy as np

a = np.array([1,2,3])
print(a)

"""NP.REPEAT, REPEAT EACH NUMBER OF AN ARRAY THE NUMBER OF TIMES YOU CHOOSE.
   NP.TILE REPEAT THE WHOLE ARRAY THE NUMBER OF TIMES YOU CHOOSE"""
new_array = np.r_[np.repeat(a,3),np.tile(a,3)]
print(new_array)

"""RESTACKING PREVIOS ARRAY"""
new_array2 = np.vstack((np.repeat(a,3), np.tile(a,3)))
print(new_array2)