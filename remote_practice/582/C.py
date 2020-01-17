# Idea: there should be a cycle for any given divisor

Q = int(input())

# Pregenerate cycles
cycles = dict()
for i in range(0,10):
    c = []
    count = 1
    while True:
        lastdigit = int(str(count*i)[-1])
        # print(i, lastdigit)
        if lastdigit not in c:
            c.append(lastdigit)
        else:
            break
        count += 1
    cycles[i] = c

for k in range(Q):
    N, M = [int(x) for x in input().split(' ')]
    numreq = N//M
    cycledata = cycles[int(str(M)[-1])]
    print(
        (numreq//len(cycledata)*sum(cycledata) +
            sum(cycledata[:numreq%len(cycledata)]))
    )
