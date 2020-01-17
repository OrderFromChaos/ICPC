from math import gcd, sqrt, ceil
from functools import reduce

# get array gcd, then factor it. Count of factors is final answer

N = int(input())
A = [int(x) for x in input().split(' ')]

allgcd = reduce(gcd, A)
# print(allgcd)

def factor(x):
    if x == 1:
        return [1]
    f = []
    for i in range(1, ceil(sqrt(x))+1): # Figure this shit out later
        if x % i == 0:
            f.append(i)
            f.append(x//i)
    return set(f)

# print(factor(allgcd))
print(len(factor(allgcd)))