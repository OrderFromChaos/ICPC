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

x = int(input())
primelist = sieveto(1000000)

stepcount = 0
# print(x)
while (x > 3):
    i = bisect_left(primelist, x)
    if i:
        i -= 1
    while i > -1:
        breakouter = False
        q = primelist[i]
        p = x-q # Target num
        for j in primelist:
            if j == p:
                x = q-p
                breakouter = True
                break
            elif j > p:
                break
        i -= 1
        if breakouter:
            break
    # print(x)
    stepcount += 1
# print()
print(stepcount)