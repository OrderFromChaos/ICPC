"""
ID: sourcef3
LANG: PYTHON3
TASK: beads
"""

#             1 2                               1 2
#         r b b r                           b r r b
#       r         b                       b         b
#      r           r                     b           r
#     r             r                   w             r
#    b               r                 w               w
#   b                 b               r                 r
#   b                 b               b                 b
#   b                 b               r                 b
#    r               r                 b               r
#     b             r                   r             r
#      b           r                     r           r
#        r       r                         r       b
#          r b r                             r r w
#         Figure A                         Figure B
#                     r red bead
#                     b blue bead
#                     w white bead

# I should have used a queue for this...

problemname = 'beads'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

data = data[1]

# Optimal breakpoint is when (number coming left) + (number coming right) is highest
# Brute force complexity: O(n^2)

def wrapStr(string, start):
    outstr = []
    for i in range(len(string)):
        outstr.append(string[start])
        start = (start+1)%len(string)
    return ''.join(outstr)

counts = []
for i, c in enumerate(data):
    # 1. Read forward
    fwdcnt = 1
    fwdChar = i
    fwdBead = c
    # print('Reading forward')
    while data[fwdChar] == fwdBead or data[fwdChar] == 'w':
        fwdcnt += 1
        fwdChar = (fwdChar+1)%len(data)
        if fwdChar == i:
            break
        # print(fwdChar, data[fwdChar])
        if fwdBead == 'w' and data[fwdChar] != 'w':
            fwdBead = data[fwdChar]
    fwdcnt -= 1
    fwdChar = (fwdChar-1)%len(data)

    # 2. Read back
    backcnt = 1
    backChar = (i-1)%len(data)
    backBead = data[backChar]
    # print('Reading back', backBead)
    while data[backChar] == backBead or data[backChar] == 'w':
        if backChar == fwdChar:
            break
        backcnt += 1
        backChar = (backChar-1)%len(data)
        # print(backChar, data[backChar])
        if backBead == 'w' and data[backChar] != 'w':
            backBead = data[backChar]
    backcnt -= 1
    
    # print('{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {}'.format(fwdcnt, backcnt, fwdcnt + backcnt, i, fwdChar, backChar, wrapStr(data,i)))
    counts.append(fwdcnt + backcnt)

with open(problemname + '.out','w') as f:
    f.write(str(max(counts)))
    f.write('\n')


