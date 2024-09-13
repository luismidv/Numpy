"""GETTING POSITIONS WHERE ELEMENTS OF TWO ARRAYS MATCH """
import numpy as np

a = np.array([10,2,5,6,7,2,3,4])
b = np.array([10,3,5,1,7,1,3,0])

print(a)
print(b)

new_array = np.where(a==b)
print(new_array)