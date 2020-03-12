# This is just greedy

N = int(input())
P = [int(x) for x in input().split()]

# Get all the removed bulbs, split them into even and odd parity.
# Characterize each spot by their complexity per type of inserted bulb
# (array of dicts {0: 0_complexity, 1: 1_complexity})

missing = set(range(1,len(P)+1)) - set(P)
odds = [x for x in missing if x % 2]
evens = [x for x in missing if x % 2 == 0]

numremoved = 0
cost = []
for i, x in enumerate(P):
    if x == 0:
        numremoved += 1

        if i != 0 and i != len(P) - 1:
            window = P[i-1:i+2]
            complexity = {
                0: window[0]%2 + window[2]%2,
                1: 1 if window[0]%2 else 0 + 1 if window[2]%2 else 0
            }
        else:
            if i == 0:
                window = [0, P[i], P[i+1]]
                complexity = {
                    0: window[2]%2,
                    1: 1 if window[2]%2 else 0
                }
            else:
                window = [P[i-1], P[i], 0]
                complexity = {
                    0: window[0]%2,
                    1: 1 if window[0]%2 else 0
                }
        print(window)
        complexity['origpos'] = i
        cost.append(complexity)

# Then replace in "least worst" order.
# Doing high complexity because it's the easiest and N <= 100.
while numremoved > 0:
    ztop = max(cost, key=lambda x: x[0])
    otop = max(cost, key=lambda x: x[1])
    if ztop[0] > otop[1]:
        # Costs a lot to put a zero here, so put a 1 here instead
        if odds:
            P[ztop['origpos']] = odds[-1]
            odds.pop()
        else:
            break # Let cleanup algo fill the rest without checks
        for i, x in enumerate(cost):
            if x['origpos'] == ztop['origpos']:
                break
        del cost[i]
    else:
        if evens:
            P[otop['origpos']] = evens[-1]
            evens.pop()
        else:
            break # Let cleanup algo fill the rest without checks
        for i, x in enumerate(cost):
            if x['origpos'] == otop['origpos']:
                break
        del cost[i]
    numremoved -= 1

if numremoved > 0:
    left = evens if evens else odds
    for i, x in enumerate(P):
        if x == 0:
            P[i] = left[-1]
            left.pop()

# Recompute complexity (we want total complexity, not just on replacement order)

print(P)

finc = 0
for i in range(1,len(P)):
    if P[i] % 2 != P[i-1] % 2:
        finc += 1

print(finc)