# Previous subproblems can be used to solve future subproblems.

def complexity(L):
    if len(L) <= 1:
        return 0
    else:
        cost = 0
        for i in range(1,len(L)):
            if L[i] % 2 != L[i-1] % 2:
                cost += 1
        return cost

