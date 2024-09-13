"""GETTING THE MAXIMUM FROM A PAIR VALUES FROM DIFFERENT ARRAYS
   """

import numpy as np

def maxx(x,y):
    if x >= y:
        return x
    else:
        return y
    
def pair_max(x,y):
    maximum = [maxx(a,b) for a,b in map(lambda a,b:(a,b),x,y)]
    return np.array(maximum)

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

array = pair_max(a,b)
print(array)