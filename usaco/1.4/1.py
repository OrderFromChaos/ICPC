"""
ID: sourcef3
LANG: PYTHON3
TASK: milk
"""

problemname = 'milk'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

N, M = [int(x) for x in data[0].split(' ')]
info = []
for i in range(M):
    info.append([int(x) for x in data[i+1].split(' ')])
info.sort(key = lambda x: x[0])

# print(info)

count = 0
total = 0
# print(N)
while N > 0:
    i = info[count]
    if i[1] <= N:
        N -= i[1]
        total += i[0]*i[1]
    else:
        total += i[0]*N
        N = 0
    count += 1
    # print(N)

# print(total)

with open(problemname + '.out','w') as f:
    f.write(str(total))
    f.write('\n')