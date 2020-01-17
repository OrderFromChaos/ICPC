Q = int(input())
for q in range(Q):
    k, n, a, b = [int(x) for x in input().split(' ')]
    aturns = (k-a) // a
    bturns = (k-b) // b
    cost = a - b
    aleftover = (k - 1) - n*b

    print(bturns, n, cost, aleftover, aturns)

    if bturns < n:
        print(-1)
    elif bturns == n:
        print(0)
    else: # Some aturns can be completed
        print(min([aleftover // cost, n, aturns]))
