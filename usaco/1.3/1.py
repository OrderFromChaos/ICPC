"""
ID: sourcef3
LANG: PYTHON3
TASK: milk2
"""

problemname = 'milk2'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

data = [[int(y) for y in x.split()] for x in data[1:]]
data = [[x[0], x[1]-1] for x in data]

alltimes = [item for sublist in data for item in sublist]

onemilk = []
nomilk = [0]
state = 0
# 0 = no cows being milked last step
# 1 = cows milked last step
for i in range(min(alltimes),max(alltimes)+1):
    milking = sum([x[0] <= i <= x[1] for x in data])
    if milking > 0:
        if state == 1: # Currently milking and was milking
            onemilk[-1] += 1
        else: # Currently milking and was not previously milking
            onemilk.append(1)
        state = 1
    else:
        if state == 0: # Not milking and was not previously milking
            nomilk[-1] += 1
        else: # Not milking and was previously milking
            nomilk.append(1)
        state = 0

# print(onemilk)
# print(nomilk)
# print(max(onemilk))
# print(max(nomilk))

with open(problemname + '.out','w') as f:
    f.write(str(max(onemilk)) + ' ' + str(max(nomilk)))
    f.write('\n')