# Compute range, output accordingly

Q = int(input())

for q in range(Q):
    N, K = [int(x) for x in input().split(' ')]
    A = [int(x) for x in input().split(' ')]
    r = max(A) - min(A)
    if r > 2*K:
        print(-1)
    else:
        print(max(A) + (K-r))