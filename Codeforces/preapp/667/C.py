from math import gcd

T = int(input())

for t in range(T):
    n, x, y = [int(x) for x in input().split()]
    # Required to be positive integers, max spacing is abs(x-y)
    # Always put max(x,y) at farthest right?

    # idea: try and take gcd(b, abs(x-y)) as the "best" spacing available
    # extend that until you hit 1, and then your "maximum" element is whatever
    # the rightmost boundary is

    if n == 2:
        print(x, y)
    else:
        dist = abs(x-y)
        for i in range(n-1, 0, -1): # Find spacing between x and y
            m, d = divmod(dist, i)
            if d == 0:
                break

        inside = dist//m + 1
        total = inside
        lefttotal = abs(min([x,y])-1)//m
        leftmost = min([x,y]) - m*min([lefttotal, n-inside])
        
        p = range(leftmost, leftmost+m*(n-1)+1, m)
        print(*p)
            