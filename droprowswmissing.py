"""DROP ROWS THAT CONTAINS MISSING VALUES"""
"""NON USABLE"""
import numpy as np

iris_data = np.genfromtxt('data3.txt', dtype = 'float', skip_header=0, usecols=[0,1,2,3,4,5,6], delimiter=",")
print(iris_data)
"""
print(len(iris_data))

pos_col = np.random.randint(0,5,1)
pos_row = np.random.randint(0,5,1)
print("Posicion de la fila", pos_row, "Posicion de la columna", pos_col)

iris_data1 = iris_data[pos_col] = np.nan
print(iris_data1)"""

iris_data1 = iris_data[np.random.randint(5, size=2), np.random.randint(4, size=2)] = np.nan
iris_data2 = iris_data1[np.sum(np.isnan(iris_data1), axis = 1) == 0][:5]
print(iris_data2)
