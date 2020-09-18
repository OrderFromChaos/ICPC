from math import gcd
from functools import reduce

n = int(input())
a = [int(x) for x in input().split(' ')]
x = max(a)
taken = [x-k for k in a]
z = reduce(gcd, taken) # Largest possible z, which means smallest possible y
y = sum(taken)//z # (missing swords)/(largest sword batch) = (smallest n of people)

print(y,z)
