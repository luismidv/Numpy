"""GET MEDIAN MEAN AND STD WITH NUMPY"""
import numpy as np

iris_data = np.genfromtxt('data.txt.txt', skip_header=0, dtype=float, delimiter = "," , usecols=[0,1,2,3,4,5,6,7])
mean = np.mean(iris_data)
median = np.median(iris_data)
std = np.std(iris_data)
print("The median of the iris_data is ", median, "The mean of the iris_data is ", mean, "The std of the iris_data is", std)
