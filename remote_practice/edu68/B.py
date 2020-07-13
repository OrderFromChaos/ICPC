# We did one kinda like this at UCRPC!

from collections import Counter
from itertools import product

Q = int(input())
for q in range(Q):
    N, M = [int(x) for x in input().split()]
    
    rows = Counter()
    columns = Counter()
    
    rows[0] = 0
    columns[0] = 0

    # Costs O(N*M)
    mat = []
    for n in range(N):
        mat.append(input())
        stars = [i for i,x in enumerate(mat[-1]) if x == '*']
        # print(stars)
        rows[n] += len(stars)
        for i in stars:
            # we're at (n, i) right now
            columns[i] += 1

    # Greedy works here. Select the max row and column and add 1 until a cross is achieved

    # print(rows)
    # print(columns)
    # print(M - max(rows.values()) + N - max(columns.values()))
    # ^^ Doesn't work on:
    # 3 3
    # .*.
    # *.*
    # .*.
    # (Same square is being replaced)

    # Costs O(N + M)
    maxr = 0
    maxc = 0
    maxrows = []
    maxcols = []
    for a, b in rows.items():
        if b > maxr:
            maxr = b
            maxrows.clear()
            maxrows.append((a,b))
        elif b == maxr:
            maxrows.append((a,b))
    for a, b in columns.items():
        if b > maxc:
            maxc = b
            maxcols.clear()
            maxcols.append((a,b))
        elif b == maxc:
            maxcols.append((a,b))
    
    # print(len(maxrows), len(maxcols))

    if (M - maxrows[0][1] + N - maxcols[0][1]) == 0:
        print(0)
        continue
    
    # If we reached here, paint squares > 0
    # Have to access mat to get blank squares

    # print(maxrow, maxcol)

    # Costs O(N*len(maxrows) + M*len(maxcols))
    best = N * M
    for pairs in product(maxrows, maxcols):
        maxrow, maxcol = pairs

        blanks = set()

        for i, x in enumerate(mat[maxrow[0]]):
            if x == '.':
                blanks.add((maxrow[0], i))

        maxcollist = [mat[i][maxcol[0]] for i in range(N)]
        for i, x in enumerate(maxcollist):
            if x == '.':
                blanks.add((i, maxcol[0]))
        
        if len(blanks) < best:
            best = len(blanks)

    print(best)