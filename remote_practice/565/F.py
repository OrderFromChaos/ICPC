Q = int(input())

for q in range(Q):
    K = int(input())
    costs = []
    cmana = 3
    for k in range(K):
        card = [int(x) for x in input().split()]
        card.append(card[1]/card[0] if card[0] != 0 else 1000000000)
        while cmana > 0:
            


