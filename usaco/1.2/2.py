"""
ID: sourcef3
LANG: PYTHON3
TASK: ride
"""
from string import ascii_uppercase
from functools import reduce

# must use sys.stderr.write('message') for logging messages
with open('ride.in','r') as f:
    data = [x.strip() for x in f.readlines()]

strtonum = lambda x: [ascii_uppercase.index(y)+1 for y in x]
numprod = lambda x: reduce(lambda a,b: a*b, x)
proc = lambda x: numprod(strtonum(x))

if proc(data[0])%47 == proc(data[1])%47:
    output = 'GO'
else:
    output = 'STAY'

with open('ride.out','w') as f:
    f.write(output)
    f.write('\n')