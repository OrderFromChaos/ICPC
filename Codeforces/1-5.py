def pos(p, val):
    if p == val:
        return 1
    elif val < p:
        return val + 1
    else:
        return val

def f(p):
    global mlist
    out = 0
    for i, x in enumerate(mlist[:-1]):
        out += abs(pos(p, mlist[i+1])-pos(p, x))
    return out

n, _ = [int(x) for x in input().split(' ')]
mlist = [int(x) for x in input().split(' ')]

for j in range(n-1):
    print(f(j+1), end=' ')
print(f(n))
