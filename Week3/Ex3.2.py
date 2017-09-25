import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

f = open ( 'pointFile.txt' , 'r')
l = [ map(float,line.split(' ')) for line in f ]

#how do i get l loaded into np.array?
xList=[]
yList=[]
for p in l:
    xList.append(p[0])
    yList.append(p[1])    

points = np.array([(1, 1), (2, 4), (3, 1), (9, 3)])

# get x and y vectors
x_ = np.array(xList)
y_ = np.array(yList)

def fit_func(x_, a, b, c, d):
    return a*x*x*x + b*x*x + c*x + d

params = curve_fit(fit_func, x, y)

print (params[0])

#maybe we should plot it?

def graph(formula, x_range,x_,y_):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)
    plt.plot(x_, y_, 'ro')
    plt.plot()
    plt.show()

graph('3*x**3+x*x-2*x+3.9', range(-20, 20),x_,y_)


#plt.plot(x,y,'o', x_new, y_new)
#plt.xlim([x[0]-1, x[-1] + 1 ])
#plt.show()

    
