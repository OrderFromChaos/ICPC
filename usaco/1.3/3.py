"""
ID: sourcef3
LANG: PYTHON3
TASK: namenum
"""

from string import ascii_uppercase
from collections import Counter

problemname = 'namenum'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

data = int(data[0])

# 1. Create number mapping
letters = list(ascii_uppercase)
letters.remove('Q')
letters.remove('Z')
# Give these an impossible number
letters.append('Q')
letters.append('Z')

numbering = []
for i in range(2,10):
    numbering += [str(i)]*3
numbering += ['0']*2

def numconv(word):
    out = []
    for c in word:
        out.append(numbering[letters.index(c)])
    return int(''.join(out))

# 2. Convert dict.txt to numbers
with open('dict.txt','r') as f:
    validnames = [x.strip() for x in f.readlines()]

numbers = [numconv(x) for x in validnames]

towrite = []
for i, x in enumerate(numbers):
    if x == data:
        towrite.append(validnames[i])

if not towrite:
    towrite.append('NONE')

with open(problemname + '.out','w') as f:
    for i in towrite:
        f.write(i)
        f.write('\n')