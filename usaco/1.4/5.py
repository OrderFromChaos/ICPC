"""
ID: sourcef3
LANG: PYTHON3
TASK: wormhole
"""

from itertools import combinations
from copy import deepcopy

problemname = 'wormhole'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

# Note that wormholes are UNdirected (A <-> B)
# Choose 2, then choose N/2, then check for cycles

N = int(data[0])
wormholes = [[int(y) for y in x.split(' ')] for x in data[1:]]

print(wormholes)

# pairs = combinations(wormholes, r=2)
# cases = combinations(pairs, r=N//2)

# Problem: cases happily outputs [((0,0), (1,0)),((0,0), (1,1))] because it is allowed to reselect (0,0) with a different pair
# Insight from https://cs.stackexchange.com/questions/11/generating-combinations-from-a-set-of-pairs-without-repetition-of-elements
#            Root
#              |
#      ----------------
#      |       |       |
#    (0,1)   (0,2)   (0,3)
#      |       |       |
#    (2,3)   (1,3)   (1,2)
# Can be solved recursively as long as information is passed. Since N is 12 at most, this is not terrible, but it's still pretty bad.
# Note that the "cases" tree has pairs of 2D vects, not just 2D vects.

cases = []

# Generate cases
def recurseSelect(left, spacing, seed):
    # Want to return pairings like [[((0,0), (1,0)), ((0,1), (1,1))], ...]
    # Method: get two lists. One is current pairing, one is recursed pairings.
    # For example:
    # one = [( (0,0), (0,1) )]
    # two = [( (1,0), (1,1) )]
    # For each pair in two, dupe one and append
    # Repeat process for each possible pair
    allpairings = []
    for i, x in enumerate(left[:-1]):
        for j, y in enumerate(left[i+1:]):
            j += i+1
            print(spacing,i,j)
            print('   ',spacing,'left', left)
            # print('   ',spacing,'one ', one)
            if len(left) > 2:
                print('   ',spacing,'splt', left[:i] + left[i+1:j] + left[j+1:])
                print('   ',spacing,'seed', seed + [(x,y)])
                two = recurseSelect(left[:i] + left[i+1:j] + left[j+1:], spacing + '    ', seed + [(x,y)])
                print('   ',spacing,'two ', two)
                # Merge
                # Check nest depth
                try:
                    two[0][0][0]
                    allpairings += two
                except:
                    allpairings.append(two)
                # one += [deepcopy(one) for x in range(max([0,len(two)-1]))]
                # if len(two) > 0:
                #     one = one*len(two)
                # for i, x in enumerate(two):
                #     one[i] += x
                # print('   ',spacing,'new one', one)
                print('   ',spacing,'new allpairings',allpairings)
            else:
                print('   ', spacing, 'Max Depth, returning', seed + [(x,y)])
                return seed + [(x,y)]
            # allpairings.append(one)
    return allpairings

cases = recurseSelect([x for x in range(len(wormholes))], '', [])
# cases = [frozenset(x) for x in cases]
# cases = set(cases)
print(cases)
raise Exception()

# Still need to get rid of identical pairings

def allunique(casecombo):
    pass

cases = [x for x in cases if allunique(x)]

def iscycle(c):
    # Have to check all possible subcycles :(
    subcycles = []
    for i in range(1, len(c)+1):
        subcycles += combinations(c,i)
    
    cyclebool = False
    seen = set()
    stepcount = 0
    for poss in subcycles:
        # Oof, writing a useful, non edge-case-missing walk is definitely the hardest part
        # In the case of (([0, 0], [0, 1]), ([1, 0], [0, 1])),
        #     an approach of "start at [0,0] and then walk forward" finds the cycle,
        #     but if it were phrased as (([0, 1], [0, 0]), ([1, 0], [0, 1])),
        #     it would not, even though those are identical. Steps could be sorted by x, though.
        # We want to find a cycle in only these two cases:
        # (([0, 0], [1, 0]), ([1, 1], [0, 1]))
        # (([0, 0], [1, 1]), ([1, 0], [0, 1]))
        # Note that combinations is returning wrong results in some cases:
        # (([0, 0], [1, 0]), ([0, 0], [0, 1]))
        #     ([0,0] shows up twice) so combinations_without_replacement is probably needed
        pass
    return cyclebool

count = 0
for i in cases:
    print(i)
    for j in iscycle(i):
        print('    ',j)
    # if iscycle(i):
    #     count += 1

print(count)



# with open(problemname + '.out','w') as f:
#     f.write(output)
#     f.write('\n')