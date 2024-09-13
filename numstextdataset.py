"""IMPORT DATASETS WITH NUMBERS AND TEXT FROM A TXT"""

import numpy as np

iris_data = np.genfromtxt('asd.txt.txt', delimiter = ',', skip_header = 1, usecols = [0,1,2,3,4,5], dtype = object)
print(iris_data)