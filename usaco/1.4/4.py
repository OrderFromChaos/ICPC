"""
ID: sourcef3
LANG: PYTHON3
TASK: combo
"""

from itertools import product

problemname = 'combo'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

N = int(data[0])
farmer = [int(x) for x in data[1].split(' ')]
master = [int(x) for x in data[2].split(' ')]

# for each digit, make list of possibilities

fposs = []
for i, x in enumerate(farmer):
    poss = [x-2,x-1,x,x+1,x+2]
    fposs.append([x%N+1 for x in poss])
mposs = []
for i, x in enumerate(master):
    poss = [x-2,x-1,x,x+1,x+2]
    mposs.append([x%N+1 for x in poss])

combos = set(list(product(*(fposs))) + list(product(*mposs)))
# print(combos)
# print(len(combos))
# print(list(product(*fposs)))
# print(list(product(*mposs)))

with open(problemname + '.out','w') as f:
    f.write(str(len(combos)))
    f.write('\n')