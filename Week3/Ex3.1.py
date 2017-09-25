import numpy as np

f = open ( 'matrixFile.txt' , 'r')

with open('matrixFile.txt') as file:
    array2d = [[int(digit) for digit in line.split(',')] for line in file]

A = np.asmatrix(array2d)
x = np.linalg.solve((A[:,0:3]), (A[:,3]))

print (x)