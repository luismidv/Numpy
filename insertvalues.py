"""INSERT VALUES ON RANDOM POSITIONS"""

import numpy as np
from random import *

iris_data = np.genfromtxt('data.txt.txt', delimiter = ",", dtype = float, skip_header=0, usecols=[0,1,2,3,4,5,6,7,8,9,10])


for i in np.random.randint(0,len(iris_data), 20):
    iris_data[i] = np.nan
print(iris_data)
