
class Node:
    def __init__(self, val):
        self.val = val
        self.connected = []
    def __repr__(self):
        return str( (self.val, self.connected) )

# Do BFS
# Red-Black color the tree
# Try odd and even ;) one will be a correct answer.

# Construct graph
Q = int(input())
for q in range(Q):
    M, N = [int(x) for x in input().split()]
    nodes = [Node(x) for x in range(1,M+1)]
    for i in range(N):
        V, U = [int(x) for x in input().split()]
        nodes[V-1].connected.append(U-1)
        nodes[U-1].connected.append(V-1)

    odds = []
    evens = []

    seen = set()
    stack = []
    stack.append( (nodes[0].val, 0) )
    while len(stack) > 0:
        # sleep(0.1)
        # print(stack)
        topnum, depth = stack.pop()
        top = nodes[topnum]
        if topnum not in seen:
            if depth % 2 == 0:
                evens.append(topnum)
            else:
                odds.append(topnum)
            seen.add(topnum)

            for i in top.connected:
                if i not in seen:
                    stack.append( (i, depth+1) )

    maxsize = M // 2
    if len(odds) <= maxsize:
        print(len(odds))
        print(' '.join([str(x) for x in odds]))
    else:
        print(len(evens))
        print(' '.join([str(x) for x in evens]))