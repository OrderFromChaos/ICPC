# Easy since no limits to amount of sorts

from collections import Counter

T = int(input())
for t in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    Bprev = 0
    Abuf = Counter()
    Bbuf = Counter()
    for Atop, Btop in zip(A,B):
        if Atop != Btop:
            Abuf[Atop] += 1
            Bbuf[Btop] += 1
            if Bprev > Btop:
                break
            else:
                Bprev = Btop
    else:
        if Abuf:
            if Abuf == Bbuf:
                # print('Non-matching terms frequencies are identical')
                print('YES')
            else:
                # print('Abuf != Bbuf')
                print('NO')
        else:
            # print('Buffer is empty, so strings already match')
            print('YES')
        continue
    # print('Non-matching B terms are in decreasing order')
    print('NO')

