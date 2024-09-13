"""CREATES A NEW ARRAY REPLACING ODD NUMBERS IN FIRST ARRAY WITH 1"""
import numpy as np

array = np.arange(10)
print(array)

"""ANOTHER WAY TO COPY ARRAYS (UNNECESARY IN MY OPINION BUT IT'S OK TO KNOW)"""
new_array = array.copy()
print(new_array)

array_condition = array[array%2 == 1] = -1
print(array_condition)
