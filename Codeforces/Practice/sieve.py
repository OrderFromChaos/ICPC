# Based on https://stackoverflow.com/questions/16004407/a-fast-prime-number-sieve-in-python
import timeit

def sieveto(n):
    size = n//2 # Only need to search odd nums for primes
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i + 1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return sieve

print([2] + [i*2+1 for i,v in enumerate(sieveto(100000)) if v and i>0])

# print(timeit.timeit(setup='from __main__ import sieveto2',
#                     stmt='sieveto2(1000000)', 
#                     number=100)/100
# )