# import numpy as np

# 5 types:
# o
# +
# .
# |
# -

# First find extent of problem
# x: (0, 12849) (-5053, 5578)
# y: (-4145, 7473) (-2319, 13994)
# Probably best to just to line intersects

import sys

wires = []
for line in sys.stdin:
    inst = [(x[0], int(x[1:])) for x in line.split(',')]
    wires.append(inst)  

prevlines = []
intersects = []
x, y = 0, 0

for ty, amt in wires[0]:
    startx, starty = x, y
    if ty == 'R':
        x += amt
    elif ty == 'D':
        y -= amt
    elif ty == 'L':
        x -= amt
    else:
        y += amt
    currline = ((startx, starty), (x, y))
    prevlines.append( currline )

x, y = 0, 0
for ty, amt in wires[1]:
    startx, starty = x, y
    if ty == 'R':
        x += amt
    elif ty == 'D':
        y -= amt
    elif ty == 'L':
        x -= amt
    else:
        y += amt
    # Check for intersects, add to intersect list
    ctype = (startx == x) # True if vertical, false if horizontal
    for i in prevlines:
        # currline = ((startx, starty), (x, y))
        if ctype:
            r = [starty, y]
            r.sort()
            if r[0] <= i[0][1] <= r[1]: # or y <= i[0][1] <= starty:
                intersects.append((x,i[1][1]))
        else:
            r = [startx, x]
            r.sort()
            if r[0] <= i[0][0] <= r[1]: # or x <= i[0][0] <= startx:
                intersects.append((i[1][0], y))

print(intersects)

mindist = 1000000000
for i in intersects[1:]:
    dist = abs(i[0]) + abs(i[1])
    # print(i, dist)
    if dist < mindist and dist != 0:
        mindist = dist
print(mindist)