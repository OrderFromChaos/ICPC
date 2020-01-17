q = int(input())
for i in range(q):
    piles = [int(x) for x in input().split(' ')]
    # take two smallest numbers and biggest number, allocate as needed
    piles.sort()
    a, b, c = piles

    c = c-(b-a)
    a = b

    if c > 0:
        c //= 2
    print(a + c)
