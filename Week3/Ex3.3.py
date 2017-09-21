import timeit

start = timeit.default_timer()
print (sumFunction(1,10000))
stop = timeit.default_timer()

print stop - start 

def sumFunction(n,m):
    result = 0
    for n in range (n,m):
        result = result + 1/float(n*n)
    return result        

def new_method():
    print("heasdfasdfsafsafj")

new_method()