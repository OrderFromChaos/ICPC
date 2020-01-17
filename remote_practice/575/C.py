q = int(input())
for query in range(q):
    n = int(input())
    for robot in range(n):
        xi, yi, fi1, fi2, fi3, fi4 = [int(x) for x in input().split(' ')]
        # oh it's a geometry problem, nevermind