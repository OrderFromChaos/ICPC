"""
ID: sourcef3
LANG: PYTHON3
TASK: palsquare
"""

from string import ascii_uppercase

problemname = 'palsquare'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

data = int(data[0])

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

outputs = []
for i in range(1,301):
    baseBsq = toBaseB(intPow(i,2), data)
    if baseBsq == baseBsq[::-1]:
        outputs.append(''.join(toBaseB(i,data)) + ' ' + ''.join(baseBsq))


# a = toBaseB(100, 10)
# print(a)

with open(problemname + '.out','w') as f:
    for i in outputs:
        f.write(i)
        f.write('\n')