from collections import Counter

T = int(input())

for t in range(T):
    # greedy select from highest number. assume this is possible.
    _ = input()
    p = [int(x) for x in input().split()]
    f = Counter(p)

    fp = [0]*(len(p)-1)
    for i, x in enumerate(p):
        if i == 0:
            continue
        else:
            fp[i-1] = x + p[i-1]
    fp.sort()

    high = fp[-1]
    print(high)
    
    # find possible methods
    methods = []
    seen = set()
    for i in p:
        if i not in seen:
            if high-i in f:
                methods.append((i, high-i))
    
    print(methods)

    # try each of the methods, excluding ones that start with the same two
    start = tuple(p[:2])
    prime = []
    for m in methods:
        if m == start:
            continue
        else:
            prime.append(m[0])
            prime.append(m[1])
            # extend greedy
            for 