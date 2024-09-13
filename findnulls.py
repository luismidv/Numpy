"""FIND NULL VALUES ON ARRAY AND REPLCAE NULL WITH 0"""

import numpy as np

iris_data = np.genfromtxt('data3.txt', skip_header=0, delimiter=",", usecols=[0,1,2,3,4,5,6])
print(np.isnan(iris_data).any())

iris_data[3,0] = np.nan

location = np.where(np.isnan(iris_data).any())
print(location)

print(np.isnan(iris_data).any())