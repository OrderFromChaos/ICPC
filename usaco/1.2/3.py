"""
ID: sourcef3
LANG: PYTHON3
TASK: gift1
"""
# must use sys.stderr.write('message') for logging messages

problemname = 'gift1'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

np = int(data[0])
people = [x for x in data[1:np+1]]

accounts = [0]*np
loc = np+1
for i in range(np):
    accnum = people.index(data[loc])
    loc += 1
    dol, splt = [int(x) for x in data[loc].split(' ')]
    accounts[accnum] -= dol
    if splt > 0:
        accounts[accnum] += dol%splt
        for j in range(splt):
            loc += 1
            accounts[people.index(data[loc])] += dol//splt
    loc += 1

with open(problemname + '.out','w') as f:
    for name, amt in zip(people, accounts):
        f.write(name + ' ' + str(amt) + '\n')