"""
ID: sourcef3
LANG: PYTHON3
TASK: skidesign
"""

from copy import deepcopy
from math import copysign

problemname = 'skidesign'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

# Pathological case for averaging two:
# [0, 17, 34, ..., 17*(N-1), 17*N + 8]
# If an algorithm averages between the last two, then the increase
# in 17*(N-1) causes a cascade of hill changes. Probably cheaper to
# decrease 17*N + 8 for non-small N.

# Each step should cause a "left" and "right" adjustment. The cheapest of the two options
# should be picked. In the case of the original input:
# 5
# 20
# 4
# 1
# 24
# 21
# 1 and 24 need adjustment.
# Step 1:
# check left, needs only adjustment of 1 to 2, so cost of 1
# check right, needs only adjustment of 24 to 23, so cost of 1
# pick any. picking left for purposes of example
# Step 2:
# check left, needs adjustment of 2 to 3, with marginal cost of 3.
# check right, needs adjustment of 24 to 23, with cost of 1.
# pick right.

N = data[0]
elevations = [int(x) for x in data[1:]]
diffs = [abs(x - elevations[i]) for i, x in enumerate(elevations[1:])]
eltadd = lambda x,y: [a+b for a,b in zip(a,b)]

adjustments = [0]*len(elevations)
for i, x in enumerate(diffs):
    # i is leftindex of diff in elevations list
    if x > 17:
        # Have to choose between two choices: left change or right change
        # Insight: only need to adjust leftmost at any given time until all satisfied (for left check)
        tempadjust = deepcopy(adjustments)
        tempelevate = deepcopy(elevations)
        leftindex = i
        rightindex = i + 1
        lcost = 0
        rcost = 0
        # left update
        while leftindex != i + 1:
            rdiff = tempelevate[leftindex+1] - tempelevate[leftindex]
            if abs(rdiff) > 17:
                # update needed
                chg = 1 if rdiff > 0 else -1
                tempadjust[leftindex] += abs(chg)
                tempelevate[leftindex] += chg
                # now adjust cost accordingly
                lcost += int(tempadjust[leftindex]**2) - int((tempadjust[leftindex]-1)**2)
                # now adjust leftindex as needed
                if leftindex != 0:
                    ldiff = tempelevate[leftindex] - tempelevate[leftindex-1]
                    if abs(ldiff) > 17:
                        leftindex -= 1
        # TODO: While this works somewhat, it requires recursive left and right updates at each step.
        # Because of the prohibitive complexity of this, it almost certainly is not the correct methodology.






# with open(problemname + '.out','w') as f:
#     f.write(output)
#     f.write('\n')