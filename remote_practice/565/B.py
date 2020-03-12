Q = int(input())

for q in range(Q):
    N = int(input())
    A = [int(x) for x in input().split()]

    # Solvable easily as N^2, but too much complexity
    # Want to merge elements from mod class 1 and 2 to make 0

    mod0 = 0
    mod1 = 0
    mod2 = 0

    for i in A:
        if i % 3 == 0:
            mod0 += 1
        elif i % 3 == 1:
            mod1 += 1
        else:
            mod2 += 1

    merge1 = min([mod1, mod2]) # Only costs 2, so optimal over 3cost
    mod1 = max([0, mod1-merge1])
    mod2 = max([0, mod2-merge1])

    print(mod0 + merge1 + mod1 // 3 + mod2 // 3)

