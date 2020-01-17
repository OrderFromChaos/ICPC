N = input()
currsum = sum([int(x) for x in N])

if currsum % 4 == 0:
    print(N)
else:
    while sum([int(x) for x in N]) % 4 != 0:
        N = str(int(N) + 1)
    print(N)