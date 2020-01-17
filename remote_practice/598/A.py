Q = int(input())

for q in range(Q):
    a, b, n, S = [int(x) for x in input().split()]
    maxremovals = S // n
    S = S - n * min([maxremovals, a])
    if S <= b:
        print('YES')
    else:
        print('NO')