# Two goals:
# 1. find alice-bob distance
# 2. find "diameter" of tree
# both can be achieved by BFS starting on alice
# 1. pass distance with queue
# 2. for each split from alice, "color" it in the queue inputs and 
#    add the max two distances from the splits + 1 (for alice's node)

from collections import deque

class Vertex:
    def __init__(self):
        self.neigh = []
    def __repr__(self):
        return str(self.neigh)

T = int(input())

for t in range(T):
    n, a, b, da, db = [int(x) for x in input().split()]
    vertices = dict()
    for v in range(n-1): # collect edges
        vnodes = [int(x) for x in input().split()]
        for vn in vnodes:
            if vn not in vertices:
                vertices[vn] = Vertex()
        l, r = vnodes
        vertices[l].neigh.append(r)
        vertices[r].neigh.append(l)
    
    # Run BFS starting on Alice's vertex
    seen = set()
    d = deque([(x, 1, i) for i, x in enumerate(vertices[a].neigh)])
    # x is vertex number, 1 is dist, i is coloring
    colormaxes = [1]*len(vertices[a].neigh)
    seen.add(a)
    for vn in vertices[a].neigh:
        seen.add(vn)
    
    bdist = -1
    while len(d) != 0:
        curr, dist, color = d.popleft()
        curr = vertices[curr]
        for nv in curr.neigh:
            if nv not in seen:
                if nv == b:
                    bdist = dist+1
                d.append((nv, dist+1, color))
                seen.add(nv)
                colormaxes[color] = max(colormaxes[color], dist+1)
    
    if len(colormaxes) == 1:
        diameter = colormaxes[0] + 1
    else:
        diameter = sum(sorted(colormaxes)[-2:]) + 1

    if bdist <= da:
        print('Alice')
    elif 2*da >= diameter:
        print('Alice')
    elif db > 2*da:
        print('Bob')
    else:
        print('Alice')
    # print(diameter)
    # print(bdist, da, diameter, db)
    # print()
