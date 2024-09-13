"""CREATE A 2D ARRAY CONTAINING RANDOM FLOATS BETWEEN 5 AND 10 AND SELECT PRECISION"""
import numpy as np

new_array = np.random.uniform(5,10, size=(5,3))
print(new_array)

"""SET DECIMAL PRECISION TO DESIRED"""
np.set_printoptions(precision=3)
print(new_array)