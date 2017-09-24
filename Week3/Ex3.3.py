import timeit

def sumFunction(n,m):

    result = 0
    for n in range (n,m):
        result = result + 1/float(n*n)
    return result        

start = timeit.default_timer()
for i in range (0, 5000):
    sumFunction(1,10000)
stop = timeit.default_timer()
print (stop - start)
