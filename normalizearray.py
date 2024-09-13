"""NORMALIZE ARRAYS SO IT'S VALUES STAYS BETWEEN 1 AND 0"""

import numpy as np

iris_data = np.genfromtxt('data.txt.txt', delimiter=",", dtype = float, usecols=[0,1,2,3,4,5,6,7,8,9,10] , skip_header=0)
print(iris_data)

iris_data1 = (iris_data - np.min(iris_data))/(np.max(iris_data)- np.min(iris_data))
print(iris_data1)
