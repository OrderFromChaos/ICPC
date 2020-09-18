# b is the gradient of decreasing a by 1

T = int(input())
for t in range(T):
    a, b, x, y, n = [int(x) for x in input().split()]

    # Check amin strategy
    copies = [a, b, x, y, n]
    aold = a
    a = max(x, a-n)
    n -= aold - a
    if n != 0:
        b = max(y, b-n)
    prod1 = a*b

    # Check bmin strategy
    a, b, x, y, n = copies
    bold = b
    b = max(y, b-n)
    n -= bold - b
    if n != 0:
        a = max(x, a-n)
    prod2 = a*b

    print(min(prod1, prod2))