"""USING SCIENTIFIC NOTATION WITH NUMPY"""

import numpy as np

np.random.seed(100)

"""1e3 is actually 1000 in scientific notation, with supress = False you are allowing scientific notation(IT'S FALSE BY DEFAULT)"""
rand_arr = np.random.random([3,3])/1e3

np.set_printoptions(suppress=False)
print(rand_arr)

np.set_printoptions(suppress=True)
print(rand_arr)