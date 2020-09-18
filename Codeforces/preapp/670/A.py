from collections import Counter

T = int(input())

for t in range(T):
    _ = input()
    a = [int(x) for x in input().split()]
    a.sort()
    freq = Counter(a)
    # print(freq)
    onerun = -1
    tworun = -1
    for c in range(0, a[-1]+1):
        if freq[c] == 1:
            onerun = c
        elif freq[c] >= 2:
            if tworun == c - 1:
                tworun = c
            onerun = c
        else:
            break
    
    # print(onerun, tworun)
    print(onerun+1 + tworun+1)