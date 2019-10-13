nodes = dict()

class Node:
    def __init__(self,num,parents=[],children=[]):
        self.num = num
        self.parents = parents
        self.children = children
    def __repr__(self):
        return str((self.num, self.parents, self.children))

test_cases = int(input())
for i in range(test_cases):
    # 1. Construct tree
    node_count = int(input())
    for _ in range(node_count-1):
        node_pair = [int(x) for x in input().split(' ')]

        if node_pair[0] in nodes:
            nodes[node_pair[0]].children = nodes[node_pair[0]].children + [node_pair[1]]
        else:
            nodes[node_pair[0]] = Node(node_pair[0],children=[node_pair[1]])

        if node_pair[1] in nodes:
            nodes[node_pair[1]].parents = nodes[node_pair[1]].parents + [node_pair[0]]
        else:
            nodes[node_pair[1]] = Node(node_pair[1],parents=[node_pair[0]])

#    for n in nodes:
#        print(nodes[n])

    # 2. Find nearest common ancestor
    two_nodes = [int(x) for x in input().split(' ')]
    common_ancestor = 0
    ancestor_history = set(two_nodes)
    while common_ancestor == 0:
#        print(two_nodes)
        for testno, test in enumerate(two_nodes):
            if nodes[test].parents != []:
                father = nodes[test].parents[0]
                if father in ancestor_history:
                    common_ancestor = father
                    break
                else:
                    two_nodes[testno] = father
                    ancestor_history.add(father)
    print(common_ancestor)
    nodes = dict()
