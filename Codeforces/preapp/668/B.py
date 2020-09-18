T = int(input())

for t in range(T):
    _ = input()
    a = [int(x) for x in input().split()]

    # Greedy cancel all positives on right negatives
    # Remaining pos sum is number of needed coins
    bank = 0
    # bankhist = [0]
    for i in a:
        if i > 0:
            bank += i
        elif i < 0:
            bank = max([0, bank+i])
        # bankhist.append(bank)
    
    # print(bankhist)
    print(bank)