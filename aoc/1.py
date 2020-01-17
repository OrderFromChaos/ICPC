import sys
from math import floor

def computemass(m):
    p = floor(m/3) - 2
    fc = 0
    if p > 0:
        fc = computemass(p)
    else:
        p = 0
    return p + fc

fuels = []
for line in sys.stdin:
    fuels.append(computemass(int(line)))

print(sum(fuels))