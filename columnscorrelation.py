"""FIND CORRELATIONS BETWEEN TWO GIVEN COLUMNS"""

import numpy as np

iris_data = np.genfromtxt('data3.txt', skip_header=0, delimiter=",", usecols=[0,1,2,3,4,5,6])

print(np.corrcoef(iris_data[:,1], iris_data[:,5]))