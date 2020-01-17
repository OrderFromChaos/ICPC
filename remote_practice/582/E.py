# Idea: at each character, you can decide what chars are available to print
# If multiple choices, print what maintains the string attributes

N = int(input())
avoids = [input(), input()]
valid = {
    'a': ['a','b','c'],
    'b': ['a','b','c'],
    'c': ['a','b','c']
}
valid[avoids[0][0]].remove(avoids[0][1])
valid[avoids[1][0]].remove(avoids[1][1])

passed = False

if 1 in [len(x) for x in valid.values()]:
    # Do this if there's no way to get to a particular character
    # from another one (even using multiple steps)

    # This is true if either a valid is length 1 (self loop)
    # OR
    # a character is not in some 2 valid pair (2 loop)
    print('NO')
elif 'c' not in valid['a'] + valid['b']:
    print('YES')
    passed = True
    finstr = ['c']*N + ['a']*N + ['b']*N
elif 'a' not in valid['b'] + valid['c']:
    print('YES')
    passed = True
    finstr = ['a']*N + ['c']*N + ['b']*N
elif 'b' not in valid['a'] + valid['c']:
    print('YES')
    passed = True
    finstr = ['b']*N + ['a']*N + ['c']*N
else:
    passed = True
    print('YES')
    counts = {
        'a': 0,
        'b': 0,
        'c': 0
    }
    curr = 'a'
    minindex = lambda x: x.index(min(x))
    finstr = []
    for i in range(3*N):
        # Pick valid next letter to minimize counts
        curr = valid[curr][minindex([counts[c] for c in valid[curr]])]
        counts[curr] += 1
        finstr.append(curr)
    # This gets us within 1 of the correct answer
    dist = [N - counts[x] for x in counts]
    if dist != [0,0,0]:
        toremove = ['a','b','c'][dist.index(-1)]
        toadd = ['a','b','c'][dist.index(1)]
        # print(dist)
        for i, x in enumerate(finstr):
            # First try and remove
            if x == toremove:
                if i == 0:
                    finstr = finstr[1:]
                    break
                elif i == len(finstr) - 1:
                    finstr = finstr[:-1]
                    break
                else:
                    if finstr[i-1] + finstr[i+1] not in avoids:
                        finstr = finstr[:i] + finstr[i+1:]
                        break
        counts[toremove] -= 1
        for i, x in enumerate(finstr):
            # Now insert
            if i == 0:
                if toadd + finstr[0] not in avoids:
                    finstr = [toadd] + finstr
                    break
            else:
                if (finstr[i-1] + toadd not in avoids and
                    toadd + finstr[i] not in avoids):
                    finstr = finstr[:i] + [toadd] + finstr[i:]
                    break
        counts[toadd] += 1

# print(valid)

if passed:
    # print(counts)
    print(''.join(finstr))
