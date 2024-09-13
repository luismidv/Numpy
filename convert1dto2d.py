"""CONVERT A 1D ARRAY TO A 2D ARRAY"""
"""DONT USE THIS"""
import numpy as np

iris_data = np.genfromtxt('asd.txt.txt', skip_header=0, delimiter = ",", usecols = [0,1,2,3], dtype = object)
print(iris_data)