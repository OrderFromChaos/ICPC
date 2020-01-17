from collections import deque

q = int(input())
for query in range(q):
    b, w = [int(x) for x in input().split(' ')]
    # BFS, I guess
    seen = set()
    # white when (x % 2 + y % 2) % 2 == 0
    # black when (x % 2 + y % 2) % 2 == 1
    if w > b:
        x, y, c = 50000000, 50000000, 'w'
    else:
        x, y, c = 50000001, 50000000, 'b'
    d = deque()
    path = []
    d.append((x, y, c))
    wcount = 0
    bcount = 0
    while not len(d) == 0:
        broke = False
        for i in range(len(d)): # Rotate deque until target-making term found.
            target = ['b','w'][w - wcount > b - bcount] # If true, more w's are needed than b's
            x, y, c = d.popleft()
            if c == target:
                broke = True
                break
            else:
                d.append((x,y,c))
        if not broke:
            x, y, c = d.popleft()
        path.append((x,y,c))
        seen.add((x,y,c))
        if c == 'w':
            wcount += 1
        else:
            bcount += 1
        if wcount > w or bcount > b:
            print('NO')
            break
        # Check connected components
        newcol = 'b' if c == 'w' else 'w'
        connected = ((x, y-1, newcol), 
                     (x-1, y, newcol), 
                     (x+1, y, newcol),
                     (x, y+1, newcol)) # all opposite color
        for c in connected:
            if c not in seen:
                d.append(c)
        if wcount == w and bcount == b:
            print(bcount, wcount)
            print('YES')
            for i in path:
                print(*i)
            break
            
