x, y, z, d = [int(x) for x in input().split()]

x, y, z, d = sorted([x,y,z,d])
# d is now guaranteed to be a+b+c

for a in range(1, 1000000000):
    b = x - a
    c = z - b
    if c == y - a and c == d - a - b:
        if all([x > 0 for x in [a,b,c]]):
            print(a,b,c)
            exit(0)