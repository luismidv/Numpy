"""CREATES A NEW ARRAY WITH ODD NUMBERS FROM FIRST ARRAY"""
import numpy as np

array = np.arange(10)
print(array)

condition_array = array[array%2 == 1]
print(condition_array)