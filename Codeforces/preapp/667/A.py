T = int(input())

for t in range(T):
    a, b = [int(x) for x in input().split()]
    d, rem = divmod(abs(a-b),10)
    if rem > 0:
        print(d+1)
    else:
        print(d)