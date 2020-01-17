# It's BFS time :)

from collections import deque
import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
    def __repr__(self):
        return str((self.children, self.parents))

# Construct graph
nodes = dict()
existing = set()
for line in list(sys.stdin):
    line = line.strip()
    x, y = line.split(')')

    if x not in existing:
        nodes[x] = Node(x)
        existing.add(x)
    if y not in existing:
        nodes[y] = Node(y)
        existing.add(y)
    
    nodes[x].children.append(y)
    nodes[y].parents.append(x)

# print(nodes)

# Do BFS starting each 0-indegree node
starts = []
for k, obj in nodes.items():
    if len(obj.parents) == 0:
        starts.append(k)

direct = 0
indirect = 0
for k in starts:
    q = deque()
    q.append((k, 0))
    seen = set()
    while len(q) > 0:
        curr, h = q.popleft()
        seen.add(curr)
        curr = nodes[curr]
        # add orbits
        direct += len(curr.parents)
        indirect += h - 1 if h > 0 else 0
        # add new q elements
        for c in curr.children:
            if c not in seen:
                q.append((c, h+1))
print(direct, indirect)
print(direct+indirect)