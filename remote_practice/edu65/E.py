from collections import defaultdict

N, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

seen = set()
after = defaultdict(set)
for num in A:
    seen.add(num)
    for sn in seen:
        after[sn].add(num)

print(after)

# leftmost = di[0]
# rightmost = di[-1]

# Guess
# lm = max(leftmost, 0)
# rm = len(A)-rightmost
# # print(leftmost, rightmost, len(di))
# print(lm, rm)
# print(lm + rm + 1)

# print(di)