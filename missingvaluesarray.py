"""FIND MISSING VALUES IN A ARRAY AND IT'S POSITIONS"""
import numpy as np

iris_data = np.genfromtxt('data.txt.txt', delimiter= ",", dtype = float, skip_header=0, usecols=[0,1,2,3,4,5,6,7,8,9,10])
missingvalues = np.isnan(iris_data[:, :]).sum()
positionofvalues = np.where(np.isnan(iris_data[:, :]))
print("Total missing values", missingvalues)
print("Missing values positions: ", positionofvalues)


