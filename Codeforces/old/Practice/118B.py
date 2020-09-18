#           0
#         0 1 0
#       0 1 2 1 0
#     0 1 2 3 2 1 0
#   0 1 2 3 4 3 2 1 0
# 0 1 2 3 4 5 4 3 2 1 0
#   0 1 2 3 4 3 2 1 0
#     0 1 2 3 2 1 0
#       0 1 2 1 0
#         0 1 0
#           0
# n = center variable

n = int(input())
spaces = ' '*2*n
for i in range(n+1):
    print(spaces,end='')
    for j in range(i):
        print(j,end=' ')
    print(i, end='')

    if i > 0:
        print(' ',end='')
        for j in range(i-1,0,-1):
            print(j,end=' ')
        print(0,end='')
    
    print()
    spaces = spaces[:-2]

spaces = '  '
for i in range(n-1, -1, -1):
    print(spaces,end='')
    for j in range(i):
        print(j,end=' ')
    print(i, end='')

    if i > 0:
        print(' ',end='')
        for j in range(i-1,0,-1):
            print(j,end=' ')
        print(0,end='')
    
    print()
    spaces = spaces + '  '