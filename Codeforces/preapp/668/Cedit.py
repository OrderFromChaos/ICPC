from collections import Counter

T = int(input())

for t in range(T):
    n, k = [int(x) for x in input().split()]
    s = input()
    decided = ['?']*k

    breakouter = False
    for i, c in enumerate(s):
        windex = i%k
        if c != '?':
            if decided[windex] not in ['?', c]:
                print('NO')
                breakouter = True
                break
            else:
                decided[windex] = c
    
    # print(decided)

    if breakouter:
        continue

    freq = Counter(decided)
    for char in freq:
        if char == '?':
            continue
        if freq[char] > k//2:
            print('NO')
            break
    else:
        print('YES')