from itertools import product
from functools import reduce

T = int(input())

for t in range(T):
    N, K, P = [int(x) for x in input().split()]
    stacks = []
    for n in range(N):
        stacks.append([int(x) for x in input().split()])
    for i, s in enumerate(stacks):
        beauty = 0
        for j, x in enumerate(s):
            beauty += x
            stacks[i][j] = (beauty, j+1)
        stacks[i].append((0,0))
    combinations = product(*stacks)

    maxbeauty = 0
    # comb = 0
    for c in combinations:
        plates = sum(x[1] for x in c)
        if plates == P:
            total = sum(x[0] for x in c)
            if total > maxbeauty:
                maxbeauty = total
                # comb = c

    print('Case #{}:'.format(t+1), maxbeauty)
    # print(comb)

    
