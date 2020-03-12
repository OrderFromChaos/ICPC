# First, everything has to be brought to +-1. Then it should be only 2 extra

N = int(input())
A = [int(x) for x in input().split()]

cost = 0
rollprod = 1
zeroenc = False

for i in A:
    if i != 1 and i != -1:
        if i == 0:
            zeroenc = True
            cost += 1
        else:
            cost += abs(i) - 1
            if i < 0:
                rollprod *= -1
    elif i == -1:
        rollprod *= -1

if rollprod == -1 and not zeroenc:
    print(cost + 2)
else:
    print(cost)