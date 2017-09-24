import timeit
def sumFunction(n, m):
    cdef int _n, _m

    _n = n
    _m = m

    result = 0
    for _n in range (_n,_m):
        result = result + 1/float(_n*_n)

    return result

def runLoop():
    cdef long start, stop
    start = timeit.default_timer()
    for i in range(0,10000):
        print sumFunction(1, 1000)
    stop = timeit.default_timer()

    print start
    print stop
    return (stop -start)