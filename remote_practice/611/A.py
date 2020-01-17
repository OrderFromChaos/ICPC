Q = int(input())

for q in range(Q):
    h, m = [int(x) for x in input().split(' ')]
    print((24-(h+1))*60 + 60-m)