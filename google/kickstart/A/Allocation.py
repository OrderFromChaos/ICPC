import heapq

T = int(input())

for t in range(T):
    N, B = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    prices = []
    for i in A:
        heapq.heappush(prices, i)
    
    count = 0
    while B > 0:
        if len(prices) == 0:
            break
        cost = heapq.heappop(prices)
        after = B - cost
        if after >= 0:
            B = after
            count += 1
        else:
            break
    
    print('Case #{}:'.format(t+1), count)