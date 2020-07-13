T = int(input())
for t in range(T):
    N,S,Y = [int(x) for x in input().split()]
    print(N-min([S,Y])+1)