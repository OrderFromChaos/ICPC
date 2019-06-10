import re

N = int(input())
numbers = []

# This is a stupidly sadistic input format
findnums = re.compile(r"-?\d+")
while True:
    numbers += [int(x) for x in findnums.findall(input())]
    if len(numbers) == N*N:
        break

# Base cases
D = dict()
for i in range(0,N):
    D[(i,-1)] = 0
    D[(-1,i)] = 0

# Do actual DP
def getEntries(rS,rE,cS,cE): # row Start, row End, column Start, column End
    # Indexing starts at 0
    if rS == rE:
        start = rS*N
        return numbers[start+cS : start+cE]
    else:
        temp = []
        for row in range(rS,rE):
            start = row*N
            temp += numbers[start+cS : start+cE+1]
        return temp

print(getEntries(1,1,0,N))
print(getEntries(0,N,1,1))

for row in range(N):
    for col in range(N):
        rowadd = sum(getEntries(row,row,0,col))
        coladd = sum(getEntries(0,row,col,col))
        print('D')
        print(rowadd, coladd)
        D[(row,col)] = max(D[(row-1,col)] + (rowadd if rowadd > 0 else 0),
                           D[(row,col-1)] + (coladd if coladd > 0 else 0) )
        for key in D:
            print('    ', key, D[key])

print(D[(N-1,N-1)])
