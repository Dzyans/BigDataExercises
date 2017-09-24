import timeit
def sumFunction(int n, int m):
    cdef int _n, _m
    cdef double result

    _n = n
    _m = m

    result = 0
    for _n in range (_n,_m):
        result = result + 1/float(_n*_n)
    return result

def runLoop():
    cdef double start, stop
    cdef double result

    start = timeit.default_timer()
    for i in range(0, 5000):
        result = sumFunction(1, 10000)
    stop = timeit.default_timer()

    print "result: " + str(result)
    return "running time: " + str(stop -start)