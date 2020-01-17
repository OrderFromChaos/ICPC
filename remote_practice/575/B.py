from itertools import combinations
from bisect import bisect_left

q = int(input())
for i in range(q):
    n, k = [int(x) for x in input().split(' ')]
    a = [int(x) for x in input().split(' ')]
    
    seen = set()
    currsum = 0
    # This is greedy and attempts to find the maximum number of r subsets
    r = []
    for index, j in enumerate(a):
        currsum += j
        if j not in seen:
            seen.add(j)
        else:
            break
        if currsum % 2 == 1:
            currsum = 0
            seen = set()
            r.append(index+1)
    if currsum != 0 or len(seen) > 0:
        print('NO')
    elif len(r) < k:
        print('NO')
    elif len(r) > k:
        # need to anneal results
        # probably costs O(N^3) or something
        # cannot be greedy (will not find minima)
        # 1 1 1 1 1 is a counterexample to 'YES' for k=2
        subsets = [(a[0:r[0]], (1,r[0]))] + [(a[r[i]:x], (i+2, x)) for i,x in enumerate(r[1:])]
        # print(subsets)
        c = combinations(subsets, r=len(r) - k + 1)
        found = False
        for j in c:
            L = [x for y in j for x in y[0]]
            rdata = [y[1] for y in j]
            # print(L)
            # print(rdata)
            if len(set(L)) == len(L):
                print('YES')
                found = True
                break
        if not found:
            print('NO')
        else:
            print(L, rdata)
            # Now r has to be reconstructed
            s, e = rdata[0][0], rdata[-1][1]
            # remove all r elements in region inclusive
            print(r, s, e)
            r = [x for x in r if x < s or x > e]
            pos = bisect_left(r, s)
            if s > 1:
                r.insert(pos, s)
                r.insert(pos+1, e)
            else:
                r.insert(pos, e)
            print(' '.join(map(str, r)))
    else:
        print('YES')
        print(' '.join(map(str, r)))
