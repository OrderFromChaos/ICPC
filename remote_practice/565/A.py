
Q = int(input())

for q in range(Q):
    N = int(input())
    count = 0
    while N != 1:
        if N % 2 == 0:
            N = N // 2
        else:
            if N % 3 == 0:
                N = N // 3 * 2
            else:
                if N % 5 == 0:
                    N = N // 5 * 4
                else:
                    print(-1)
                    break
        count += 1
    else:
        print(count)
