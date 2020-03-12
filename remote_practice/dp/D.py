# GilDONG can only place and remove blocks at his feet.

Q = int(input())

for q in range(Q):
    N, M, K = [int(x) for x in input().split()]
    H = [int(x) for x in input().split()]
    bagbal = M
    for i, x in enumerate(H):
        # print(bagbal)
        if i != len(H) - 1:
            if x > H[i+1] - K:
                bagbal += x - max([0, H[i+1] - K ])
            else:
                bagbal -= ( H[i+1] - K ) - x
        # print(bagbal)
        if bagbal < 0:
            print('NO')
            break
    else:
        print('YES')