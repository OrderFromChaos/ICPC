
class Node:
    def __init__(self, val):
        self.val = val
        self.connected = []
        self.parity = -1
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

    odds = 0
    evens = 0

    seen = set()
    stack = []
    stack.append( (nodes[0].val, 0) )
    while len(stack) > 0:
        # sleep(0.1)
        # print(stack)
        topnum, depth = stack.pop()
        top = nodes[topnum]
        if topnum not in seen:
            parity = depth % 2
            if parity:
                odds += 1
            else:
                evens += 1
            nodes[topnum].parity = parity
            seen.add(topnum)

            for i in top.connected:
                if i not in seen:
                    stack.append( (i, depth+1) )

    maxsize = M // 2
    if odds <= maxsize:
        print(odds)
        print(' '.join([str(x.val) for x in nodes if x.parity]))
    else:
        print(evens)
        print(' '.join([str(x.val) for x in nodes if x.parity == 0]))