import numpy

f = open ( 'matrixFile.txt' , 'r')
l = [ map(int,line.split(',')) for line in f ]

a = numpy.array([[l[0][0],l[1][0],l[2][0]], [l[0][1],l[1][1],l[2][1]],[l[0][2],l[1][2],l[2][2]]])
b = numpy.array([l[0][3],l[1][3],l[2][3]])
x = numpy.linalg.solve(a, b)

print (x)
