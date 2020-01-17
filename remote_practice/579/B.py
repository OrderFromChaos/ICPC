# Count, remove 2 for each side pair. If no 2s still exist, break and 'NO'
from collections import Counter

Q = int(input())
for q in range(Q):
    N = int(input())
    sf = Counter([int(x) for x in input().split(' ')])
    print(sf)
    maxrect = sum([c // 2 for x, c in sf.items()])//2
    print(maxrect, N)