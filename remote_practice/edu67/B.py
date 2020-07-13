# Counter by left of position

from collections import Counter
from bisect import bisect_left

# class myCounter(Counter):
#     def __le__(self, other):
#         return (self.maps[0] & others.maps[0]) == self.maps[0]

_ = int(input())
S = input()
# Prepare S
freqs = [Counter()]
buffer = []
for c in S:
    buffer.append(c)
    if len(buffer) > 0 and len(buffer) % 5 == 0:
        freqs.append(freqs[-1] + Counter(buffer))
        buffer.clear()

M = int(input())
for m in range(M):
    # Now do binary search over the Counter list
    # fsearch = myCounter(input())
    # print(bisect_left(freqs, fsearch))
    f = Counter(input())
    for i in freqs:
        if (f & i) == f:
            print(f)
            print('    ', i)
            break
    else:
        print(f'No match found for {f}')
