"""
ID: sourcef3
LANG: PYTHON3
TASK: dualpal
"""

problemname = 'dualpal'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

N, S = [int(x) for x in data[0].split(' ')]

def intPow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        y = intPow(x, n//2)
        if n % 2 == 0:
            return y*y
        if n % 2 == 1:
            return y*y*x

def toBaseB(N10, B):
    # Find largest significant digit in B representation of N10
    power = 0
    while intPow(B, power) <= N10:
        power += 1
    if power > 0:
        power -= 1
    # print(power)

    newnum = [0]*(power+1)
    pos = 0
    # Explicitly convert
    while N10 > 0:
        newnum[pos] = N10//intPow(B, power)
        N10 = N10%intPow(B, power)
        power -= 1
        pos += 1

    for i, x in enumerate(newnum):
        if x > 9:
            newnum[i] = ascii_uppercase[x%10]
        else:
            newnum[i] = str(newnum[i])
    
    return newnum

pals = []
counter = S+1
while len(pals) < N:
    pcount = 0
    for base in range(2,11):
        Brep = toBaseB(counter, base)
        if Brep == Brep[::-1]:
            pcount += 1
        if pcount > 1:
            break
    if pcount > 1:
        pals.append(counter)
    counter += 1

# print(pals)

with open(problemname + '.out','w') as f:
    for i in pals:
        f.write(str(i))
        f.write('\n')