# BFS (kinda)
# Heavy use of sets

from collections import defaultdict, deque
from time import sleep

N, M = [int(x) for x in input().split()]

groups = defaultdict(list)
membership = defaultdict(list)
seen = set()

gnum = 0
maxusr = 0
for m in range(M):
    g = [int(x) for x in input().split()]
    for i in range(g[0]):
        membership[g[i+1]].append(gnum)
        groups[gnum].append(g[i+1])
        seen.add(g[i+1])
        if g[i+1] > maxusr:
            maxusr = g[i+1]
    groups[gnum] = set(groups[gnum])

    gnum += 1

# print(groups)
# print(membership)
# print(seen)

spreadcount = {x:0 for x in seen}
while len(seen) > 0:
    # print(seen)

    start = seen.pop()
    # print(start)
    d = deque()
    d.extend(membership[start])
    subgroups = set()
    subseen = set()
    subseen.add(start)
    for subg in d:
        subgroups.add(subg)

    while d:
        # print('upcoming:', d)
        # print('groups:', subgroups)
        # print('people:', subseen)
        # print()
        cg = d.popleft()
        for usr in groups[cg]:
            if usr not in subseen:
                subseen.add(usr)
                for gr in membership[usr]:
                    if gr not in subgroups:
                        subgroups.add(gr)
                        d.append(gr)
    # print('people:', subseen)
    for aff in subseen:
        spreadcount[aff] = len(subseen)
        seen.discard(aff)
    # sleep(0.1)
    # print()

output = []
for i in range(1, maxusr+1):
    if i in spreadcount:
        output.append(str(spreadcount[i]))
    else:
        output.append('1')

print(' '.join(output))