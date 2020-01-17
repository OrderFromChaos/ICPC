"""
ID: sourcef3
LANG: PYTHON3
TASK: friday
"""
# must use sys.stderr.write('message') for logging messages

from copy import deepcopy

problemname = 'friday'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

N = int(data[0])
# Populate monthlengths
monthlen = [31]*12
monthlen[1] = 28
monthlen[8] = 30
monthlen[3] = 30
monthlen[5] = 30
monthlen[10] = 30
leaplen = deepcopy(monthlen)
leaplen[1] = 29
# print(monthlen)

date = {
    'd': 1,
    'm': 1,
    'y': 1900,
    'weekday': 2
}

freq = [0]*7
while True:
    if date['d'] == 1: # Base case
        date['d'] = 13
        date['weekday'] = (date['weekday']+12%7)%7
    elif date['m'] == 12: # Year end case
        date['m'] = 1
        date['y'] += 1
        if date['y'] > 1900+N-1:
            break # Don't count the January 13th
        date['weekday'] = (date['weekday']+31%7)%7
    else:
        if date['y'] % 4 == 0 and (not date['y'] % 100 == 0 or date['y'] % 400 == 0):
            date['weekday'] = (date['weekday']+leaplen[date['m']-1]%7)%7
        else:
            date['weekday'] = (date['weekday']+monthlen[date['m']-1]%7)%7
        date['m'] += 1
    
    freq[date['weekday']] += 1

# print(freq)

with open(problemname + '.out','w') as f:
    f.write(' '.join([str(x) for x in freq]))
    f.write('\n')
