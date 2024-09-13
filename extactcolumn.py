"""SELECT SPECIFIC COLUMNS FROM ARRAYS FROM A TXT"""
import numpy as np

data = np.genfromtxt('asd.txt.txt', delimiter = ',', dtype = object, skip_header=0, usecols = [-1])
print(data)
