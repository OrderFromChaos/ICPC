# BFS (kinda)
# Heavy use of sets

from itertools import islice

N, M = [int(x) for x in input().split()]

groups = []
for m in range(M):
    g = [int(x) for x in input().split()]
    if g[0] == 0:
        continue
    pairfound = -1
    buf = []
    for i in range(g[0]):
        x = g[i+1]
        buf.append(x)
        for j, s in enumerate(groups):
            if x in s:
                pairfound = j
                break
        
        if pairfound != -1:
            break
    
    if pairfound != -1:
        for usr in buf:
            groups[j].add(usr)
        for usr in islice(g, i+1, None):
            groups[j].add(usr)
    else:
        buf.extend(islice(g, i+1, None))
        groups.append(set(buf))

# print(groups)

c = dict()
maxusr = 0
for g in groups:
    cnt = len(g)
    for usr in g:
        if usr > maxusr:
            maxusr = usr
        c[usr] = cnt

# print(c)

ans = []
for i in range(1, N+1):
    ans.append(str(c.get(i, 1)))

print(' '.join(ans))


    

# gnum = 0
# maxusr = 0
# for m in range(M):
#     g = [int(x) for x in input().split()]
#     for i in range(g[0]):
#         membership[g[i+1]].append(gnum)
#         groups[gnum].append(g[i+1])
#         seen.add(g[i+1])
#         if g[i+1] > maxusr:
#             maxusr = g[i+1]
#     groups[gnum] = set(groups[gnum])

#     gnum += 1