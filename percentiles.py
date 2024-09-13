"""CALCULATE PERCENTILES SCORES OF A NUMPY ARRAY"""

import numpy as np

iris_data = np.genfromtxt('data.txt.txt', delimiter= ",", dtype = float, skip_header=0, usecols=[0,1,2,3,4,5,6,7,8,9,10])

percentile5  = np.percentile(iris_data, q = [5])
percentile95 = np.percentile(iris_data, q = [95])
print("Percentile 5" , percentile5, "Percentile 95 ", percentile95)

