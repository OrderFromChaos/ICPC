N, K = [int(x) for x in input().split()]
S = input()
K = input().split()
K = set(K)

substr = 0

N = 0
for i in S:
    if i in K:
        N += 1
    else:
        substr += N*(N+1)//2
        N = 0

if N != 0:
    substr += N*(N+1)//2

print(substr)