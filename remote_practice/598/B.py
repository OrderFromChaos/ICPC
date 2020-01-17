from itertools import permutations

def lexicost(L):
    cost = 0
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            cost += 1
    return cost

# n = 100, so brute force is not possible (100!/0!)