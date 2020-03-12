from bisect import bisect_left
from math import gcd, sqrt
import heapq

# Sort list, work backwards. General idea is correct here.

def sieveto(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1, limit):
        if sieve[i]:
            val = 2*i + 1
            tmp = ((size-1) - i) // val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i,v in enumerate(sieve) if v and i > 0]

primes = sieveto(2800000)
primeset = set(primes)

N = int(input())
A = [int(x) for x in input().split()]
A.sort(reverse=True)

for i in A:
    # If prime do thing

    # If not prime do thing
    pass


aprimes = []
nprimes = []
for i in A:
    if i in primeset:
        aprimes.append(i)
    else:
        nprimes.append(i)

# Steps after this:
# 1. In nprimes, find max divisor for each.
# 2. Using the largest nprimes, cross off nprimes and aprimes until there are no nprimes left.
# 3. If there are remaining aprimes, check if ap == primes.index(ap) (binsearch). If so, that's another pair to cross off.
# 4. At this point there should be no remaining pairs left.

# Remaining questions:
# 1. How to optimally find max divisor?

memo = dict()
def modfactor(n):
    if n in memo:
        return memo[n]

    highest = -1
    for i in range(2, min([(sqrt(n) // 1) + 1, n-1])):
        if n % i == 0:
            highest = n // i
            break
    memo[n] = highest
    return highest

maxfact = [modfactor(n) for n in nprimes]


