# Use a Trie
# https://en.wikipedia.org/wiki/Trie
# Difference from standard implementation: put a +1 int where a string ends.
# Then call recursively from top to determine the best possible grouping sum.
# Note that each group must have at least two strings in it.

class Node:
    def __init__(self, length):
        self.children = dict() # string: int
        self.length = length
        self.ends = 0
        self.travcount = 1
    def __repr__(self):
        return str((self.children, self.length, self.ends, self.travcount))

T = int(input())
for t in range(T):
    N, K = [int(x) for x in input().split()]
    S = []
    for i in range(N):
        S.append(input())

    # print(S)

    # Construct trie
    nodes = [Node(0)]
    head = nodes[0]
    head.travcount -= 1
    currpos = 0
    endindices = []
    for s in S:
        # print(s)
        curr = head
        curr.travcount += 1
        for c in s:
            if c in curr.children:
                # Traverse down trie
                currpos = curr.children[c]
                curr = nodes[currpos]
                curr.travcount += 1
            else:
                # Make new nodes
                nodes.append(Node(curr.length+1))
                currpos = len(nodes)-1
                curr.children[c] = currpos
                curr = nodes[-1]
        nodes[currpos].ends += 1 # Add to number of strings that halt here
        endindices.append(currpos)

    # for i in nodes:
    #     print((i.children, i.length, i.travcount, i.ends))

    # Oops, can't call recursively because could reach recursion limit. (10^6 possible size)

    # Going to use recursion anyway to get the free points
    def getBiggestGrouping(node) -> (int, int, int, Node):
        # A: First int is points already found
        # B: Second int is number of available ends
        # C: Third int is ends used in total
        # D: Last matched on Node
        # Guaranteed: B <= C
        if len(node.children) == 0: # ie a leaf
            if node.ends >= 2:
                return (node.length, node.ends-2, node.ends)
            else:
                return (0, node.ends, node.ends, 0)
        else:
            a, b, c = 0, 0, 0
            D = 0
            for i in node.children.values():
                A, B, C, D = getBiggestGrouping(nodes[i])
                if node == head:
                    if B > 0:
                        # So instead, when we reach head, if there's b=1 from any branches,
                        # for each branch, go to the last matched node (newly passed up the tree now...)
                        # and match instead at the next node with multiple children.
                        # This is guaranteed, I think.
                        

                print(nodes[i])
                a += A
                b += B + node.ends
                c += C
            if b >= 2:
                b -= 2
                a += node.length
                D = node
            
            print(A,B,C, D)
            # else:
                # Force pairing if travcount would be 1 when reach head
                # But we don't have that information at this step :(
                
                # So instead, when we reach head, if there's b=1 from any branches,
                # for each branch, go to the last matched node (newly passed up the tree now...)
                # and match instead at the next node with multiple children.
                # This is guaranteed, I think.

            return (a, b, c, D)

    print('Case #{}:'.format(t+1), getBiggestGrouping(head)[0])
