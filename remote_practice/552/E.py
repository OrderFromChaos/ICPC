N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

locations = {x:i for x in enumerate(A)}

next_unchosen = list(range(N))

