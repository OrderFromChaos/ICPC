# Greedy: only need to check nearest two houses?

from collections import Counter, deque

_ = input()
X = [int(x) for x in input().split()]
f = Counter(X)
pop = [f[x] for x in range(1, max(X)+1)]
print(pop)

high, low = 0, 0
q = deque()
for i, x in enumerate(set(X)):
    # Generate possiblities
    if i > 0:
        # min stays same if prev exists. if not, min += 1
        if f[x-1] > 0:
            low += 1
    




# Min
# Want to pick houses in the middle of the stream
# eg 3 4 5 means pick house 4 to meet at
# optimal house may be either even or odd