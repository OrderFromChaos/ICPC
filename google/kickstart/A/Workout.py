import heapq

T = int(input())
for t in range(T):
    N, K = [int(x) for x in input().split()]
    M = [int(x) for x in input().split()]

    diffs = []
    for i in range(1, len(M)):
        d = M[i]-M[i-1]
        heapq.heappush(diffs, -d)

    # print(diffs)

    # Limitation:
    # Needs to be an integer number of minutes
    for k in range(K):
        d = heapq.heappop(diffs)
        # print(d, i, d//2)
        # print(diffs)
        if d == -1: # Not allowed to go under integer difficulty
            break
        if d % 2 == 0:
            # TODO: Fix these indices later
            heapq.heappush(diffs, d//2)
            heapq.heappush(diffs, d//2)
        else:
            heapq.heappush(diffs, d//2)
            heapq.heappush(diffs, d//2 + 1)
        # print(diffs)

    print('Case #{}:'.format(t+1), -1*heapq.heappop(diffs))