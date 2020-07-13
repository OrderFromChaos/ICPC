# Reverse priority queue?

import heapq

Q = int(input())
for q in range(Q):
    N, R = [int(x) for x in input().split()]
    h = [-int(x) for x in input().split()]
    heapq.heapify(h)
    # Now h is a minheap with negative elements, making it a max (abs) heap
    count = 0
    seen = set()
    push = 0
    while len(h):
        rightmost = heapq.heappop(h)
        # print(rightmost)
        if rightmost not in seen:
            if rightmost + push < 0:
                # print(rightmost+push)
                count += 1
                push += 2
                seen.add(rightmost)
            else:
                break # All subsequent monsters are dead in traps

    print(count)