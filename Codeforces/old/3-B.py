# Algorithm:
# 1. Sieve up to max(b,d). Store in primelist
# 2. Use binary search for a, b, c, d over primelist.
#    This defines your [a,b] [c,d] lists.
# 3. print(len[a,b] * len[c,d])
# 4. Complete!

# This is wrong, we do have to use GCD.
# This is apparently the "totient" - look here:
# https://en.wikipedia.org/wiki/Euler%27s_totient_function
# Any correct implementation is [d-c]*(totient complexity).
# Also, it looks like canonical totient is 1 to n, so need to offset somehow. (1->b)-(1->a) probably.

from bisect import bisect_left

def sieveto(n):
    size = n//2 # Only need to search odd nums for primes
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i + 1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i,v in enumerate(sieve) if v and i>0]

a, b, c, d = [int(x) for x in input().split(' ')]
primelist = sieveto(max([b,d]))

def uniqueprimefactors(n):
    global primelist
    relevant = primelist[:bisect_left(primelist, int(n**0.5)+1)+1]
    simplefactors = []
    for p in relevant:
        while n % p == 0:
            simplefactors.append(p)
            n = n // p
    return set(simplefactors)

def totient(n):
    global primelist
    factorization = uniqueprimefactors(n)
    prod = 1
    for p in factorization:
        prod *= 1-1/p
    return int(n*prod)

pairs = 0
if (b < d) {
    minregion = primelist[bisect_left(primelist, a):bisect_left(primelist, b)+1]
    for i in range(c,d+1):
        pairs += 
} else {
    minregion = primelist[bisect_left(primelist, c):bisect_left(primelist, d)+1]
}


