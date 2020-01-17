"""
ID: sourcef3
LANG: PYTHON3
TASK: crypt1
"""

from itertools import permutations

problemname = 'crypt1'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

digitset = set([x for x in data[1].split(' ')])
digits = list(digitset)

len3 = list(set(permutations(digits*3, r=3)))
len2 = list(set(permutations(digits*2, r=2)))

# print(len3)
# print(len2)

solutions = 0
proof = []
for i in len3:
    x = int(''.join(i))
    for j in len2:
        a, b = [int(q) for q in j]
        xa = list(str(x*a))
        if len(xa) == 3:
            if all([q in digitset for q in xa]):
                xb = list(str(x*b))
                if len(xb) == 3:
                    if all([q in digitset for q in xb]):
                        if all([q in digitset for q in list(str(x*a+x*b*10))]):
                            solutions += 1
                            proof.append([x, int(str(a) + str(b)), x*a, x*b, x*a+x*b*10])

# print(solutions)
# print(digits)
# print(proof)

with open(problemname + '.out','w') as f:
    f.write(str(solutions))
    f.write('\n')