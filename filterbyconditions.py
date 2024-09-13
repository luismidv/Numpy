"""FILTER ARRAY BASED ON TWO OR MORE CONDITIONS"""

import numpy as np

iris_data = np.genfromtxt('data2.txt', delimiter= ",", dtype = float, skip_header=0, usecols=[0,1,2,3])

iris_data1 = iris_data[iris_data[:,0] < 5]
iris_data2 = iris_data[iris_data[:,2] < 3]
print(iris_data2)
