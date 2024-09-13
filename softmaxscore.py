"""SOFTMAX IS A FUNCTION USED ON NETURAL NETWORKS"""

import numpy as np

iris_data = np.genfromtxt('data.txt.txt', delimiter= ",", dtype = float, usecols=[0,1,2,3,4,5,6,7,8,9,10], skip_header=0)
softmax = np.exp(iris_data)/sum(np.exp(iris_data))
print(softmax)
softmax1 = softmax.sum()
print(softmax1)