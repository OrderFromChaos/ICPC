"""
ID: sourcef3
LANG: PYTHON3
TASK: barn1
"""

problemname = 'barn1'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

M, S, C = [int(x) for x in data[0].split(' ')]

distances = [int(x) for x in data[1:]]
distances.sort()
if M > 1 and M < C:
    diffs = [(x-distances[i], i) for i,x in enumerate(distances[1:])]
    diffs.sort(key=lambda x: x[0])
    probdiffs = [x[0] for x in diffs[:-M+1]]
elif M == 1:
    probdiffs = [max(distances) - min(distances)]
elif M >= C:
    probdiffs = [C-M]

print(probdiffs)

with open(problemname + '.out','w') as f:
    f.write(str(sum(probdiffs) + M))
    f.write('\n')