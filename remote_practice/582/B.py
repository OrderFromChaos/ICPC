import sys

T = int(input())

for i in range(T):
    _ = input()
    data = [int(x) for x in input().split(' ')]
    badcount = 0
    currMin = data[-1]
    first = True
    for j in reversed(data):
        if first:
            first = False
        else:
            if j > currMin:
                badcount += 1
            elif j < currMin:
                currMin = j
    print(badcount)
