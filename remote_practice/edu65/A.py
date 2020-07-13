# I've seen this one :)

from collections import Counter

T = int(input())
for t in range(T):
    _ = input()
    s = input()
    if len(s) >= 11:
        if '8' in Counter(s[:-10]):
            print('YES')
            continue
    print('NO')