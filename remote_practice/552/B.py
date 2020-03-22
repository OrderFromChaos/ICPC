N = int(input())
A = [int(x) for x in input().split()]

# Range needs to be even, and D = range/2.

# Find max and min
nval = A[0]
xval = A[0]
for i in A:
    if i > xval:
        xval = i
    elif i < nval:
        nval = i

range = xval - nval
mid = nval + range/2

# print(nval, mid, xval)

if range % 2 == 1:
    # If all values are all nval and xval, this is okay (just select D = range)
    count = [0,0,0]
    for i in A:
        if i == nval:
            count[0] += 1
        elif i == xval:
            count[1] += 1
        else:
            count[2] += 1
    checks = [x > 0 for x in count]
    if checks == [1, 1, 0]:
        print(range)
    else:
        print(-1)
else:
    allowed = set([nval, xval, mid])
    for i in A:
        if i not in allowed:
            print(-1)
            exit(0)
    print(range//2)