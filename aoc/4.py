def increasing(n):
    s = str(n)
    d = [int(x) for x in s]
    for i, digit in enumerate(d[1:]):
        if digit - d[i] < 0:
            return False
    return True

def adjacentpair(n):
    s = str(n)
    d = [int(x) for x in s]
    count = dict()
    for i, digit in enumerate(d[1:]):
        if digit == d[i]:
            if digit in count:
                count[digit] += 1
            else:
                count[digit] = 1
    return any([x == 1 for x in count.values()])

start, end = [int(x) for x in input().split('-')]

ans = 0
for i in range(start, end+1):
    if increasing(i) and adjacentpair(i):
        ans += 1

print(ans)