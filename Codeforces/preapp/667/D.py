T = int(input())
for t in range(T):
    n, s = [int(x) for x in input().split()]
    # INCREASE n by 1 (!!!)

    # Strategy:
    # check first n digits
    # if rollsum goes over s, check old rollsum +1. if that's too big,
    # you have to round to the next 1000...x to reset. Otherwise you can find
    # some digit setup with right priority.

    # eg 728 10
    # breaks on 8 (rollsum: 17, oldrollsum: 9)
    # 9+1 <= 10, so 730 is the output number

    # eg 745 10
    # breaks on 4 (rollsum: 11, oldrollsum: 7)
    # 7+1 <= 10, so 802 is the output number

    if n == s:
        print(0)
        continue

    oldrollsum = 0
    rollsum = 0

    strn = str(n)

    for i, d in enumerate(strn):
        oldrollsum = rollsum
        rollsum += int(d)
        # print('   ', rollsum)
        if rollsum >= s:
            break
    
    if oldrollsum != 0 and oldrollsum + 1 <= s:
        base = int(strn[:i-1] + str(int(strn[i-1])+1) + '0'*(len(strn)-i))
    else:
        base = int('1' + '0'*len(strn))
    
    # # Now adjust with right priority until s is reached
    # digitsum = sum([int(x) for x in str(base)])
    # if digitsum > 0:
    #     m, d = divmod(s-digitsum, 9) # Find how many 9s are needed
    #     fin = base + int(str(d) + '9'*m)
    # else:
    #     fin = base
    # moves = fin - n

    # print(base, m, d, fin)
    print(base - n)
