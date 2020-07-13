T = int(input())

for t in range(T):
    X, Y = [int(x) for x in input().split()]
    if Y + 2 <= X:
        print('YES')
    else:
        print('NO')