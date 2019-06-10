class Node:
    def __init__(self, pos, edge = []):
        self.pos = pos
        self.edge = edge
    def __repr__(self):
        return str((self.pos, self.edge))

knight_squares = [(-2,-1),
        (-1,-2),
        (1,-2),
        (2,-1),
        (2,1),
        (1,2),
        (-1,2),
        (-2,1)]

xdim = int(input())
ydim = int(input())
nodes = []
node_pos = dict()

# Initialize nodes
index = 0
for x in range(xdim):
    for y in range(ydim):
        nodes.append(Node((x,y),edge=[]))
        node_pos[(x,y)] = index
        index += 1

onboard = lambda loc, board_dims: (0 <= loc[0] < board_dims[0]) and (0 <= loc[1] < board_dims[1])
add2d = lambda v1, v2: (v1[0] + v2[0], v1[1] + v2[1])

# Add edges
for n in nodes:
    for possible in knight_squares:
        loc = add2d(n.pos, possible)
        if onboard(loc, (xdim, ydim)):
            nodes[node_pos[n.pos]].edge.append(loc)

# Do DFS, prune routes that end with no possible moves
# DFS is probably slightly more optimal than BFS
found_all_visit = False
for startnode in nodes:
    visited = [startnode.pos]
    q = [(x,visited) for x in startnode.edge]
    while q: # nonempty
        pos, visited = q.pop()
        # get all new squares, add to q
        visited.append(pos)
        if len(visited) == xdim*ydim:
            found_all_visit = True
            break
        for i in nodes[node_pos[pos]].edge:
            if i not in visited:
                q.append((i,visited))
    if found_all_visit:
        break

if found_all_visit:
    print(visited)
else:
    print('impossible')
