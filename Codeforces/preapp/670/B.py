import heapq
from collections import deque

T = int(input())

for t in range(T):
    _ = input()
    A = [int(x) for x in input().split()]
    # Want to pick:
    # Even number of negatives
    # Maximum absolute value (where it doesn't conflict with the last rule)
    # Since 5 values, maximum of 4 negatives, so just pop off the 4 min at the end

    neg = []
    pos = []
    for a in A:
        if a < 0:
            heapq.heappush(neg, a)
        else:
            heapq.heappush(pos, -a) # Minheap by default

    def prodr(L):
        rollprod2 = 1
        if len(L) == 0:
            return -10000000000
        for term in L:
            rollprod2 *= term
        return rollprod2
    
    final = []
    # Pop up to 5 off posheap
    numpos = 0
    while len(pos) > 0 and numpos < 5:
        final.append(-heapq.heappop(pos))
        numpos += 1
    
    if numpos == 0:
        # Worst case scenario, need to pop everything
        # Want only smallest negatives (so therefore max product)
        larg = heapq.nlargest(5, neg)
        print(prodr(larg))
        continue

    # Pop up to 5 off negheap
    numneg = 0
    while len(neg) > 0 and numneg < 5:
        final.append(heapq.heappop(neg))
        numneg += 1
    
    final.sort() # 10 elements at most
    # print(final)

    rollprod = 1

    # print(final)
    for i in range(2): # Select two at a time
        left = prodr(final[:2])
        right = prodr(final[-2:])
        # print(left, right)
        if left >= right or numpos == 2: # [-2 -1 10 20] if pos selected, negative result
            rollprod *= left
            final = final[2:]
        else:
            rollprod *= right
            final.pop()
            final.pop()
            numpos -= 2
    rollprod *= final[-1]
    print(rollprod)
    # print()