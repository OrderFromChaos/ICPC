N, M = [int(x) for x in input().split()]

# Set up rules so they can be queried per location
rulelookup = [[] for x in range(N)]
rules = []
for m in range(M):
    T, L, R = [int(x) for x in input().split()]
    # First index doesn't matter, only subsequent indices
    rules.append([T, L+1, R, False])
    # print(rules)
    for i in range(L+1, R+1):
        rulelookup[i-1].append(m)

# print()

# Now construct the array
curr = 10000
lastdec = -1
A = []
for n in range(N):
    indrule = rulelookup[n]
    if indrule:
        actrule = [rules[i] for i in indrule]
        # print(actrule)
        # print(actrule)
        types = set([r[0] for r in actrule])
        if len(types) > 1:
            # Only needs 1 index to be decreasing
            A.append(curr)
        else:
            types = list(types)
            if types[0] == 0:
                # Do decreasing order
                curr -= 1
                A.append(curr)
                for i in indrule:
                    if rules[i][0] == 0 and rules[i][-1] == False:
                        rules[i][-1] = True
            else:
                # Do same (technically increasing, not strictly)
                A.append(curr)
    else:
        A.append(curr)

if any([(r[0] == 0 and r[-1] == False) for r in rules]):
    print('NO')
else:
    print('YES')
    print(' '.join([str(x) for x in A]))