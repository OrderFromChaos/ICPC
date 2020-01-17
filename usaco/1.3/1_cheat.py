"""
ID: sourcef3
LANG: PYTHON3
TASK: milk2
"""

problemname = 'milk2'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

data = [[int(y) for y in x.split()] for x in data[1:]]

# Concatenate all overlapping times (eg (300, 1000) + (700, 1200) = (300,1200))
# Then max(at least 1) = biggest difference, and max(none) = max(gaps)

def mergeable(a, b):
    # Only not mergeable if completely disjoint
    if b[0] > a[1] or b[1] < a[0]:
        return False
    else:
        return True

currPos = 0
while currPos < len(data) - 1:
    checkPos = currPos + 1
    merged = False
    while checkPos < len(data):
        if mergeable(data[currPos],data[checkPos]):
            data[currPos] = [min([data[currPos][0],data[checkPos][0]]),
                             max([data[currPos][1],data[checkPos][1]])]
            del data[checkPos]
            merged = True
        checkPos += 1
    if not merged:
        currPos += 1

data = sorted(data)
# print(data)

diffs = [x[1]-x[0] for x in data]
gaps = [x[0]-data[i][1] for i,x in enumerate(data[1:])]

# print(diffs)
# print(gaps)
# print(max(diffs))
# print(max(gaps))

maxdiff = max(diffs) if diffs else 0
maxgap = max(gaps) if gaps else 0

with open(problemname + '.out','w') as f:
    f.write(str(maxdiff) + ' ' + str(maxgap))
    f.write('\n')