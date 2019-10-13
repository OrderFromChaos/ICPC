A = [1,0] # Base cases, starting at n=1
C = [0,1]
D = [0,3]

for n in range(3,30):
    n = n-1 # Offset
    A.append(D[n-1]+C[n-1])
    C.append(A[n-1])
    D.append(D[n-2]+2*C[n])

usernum = int(input())
while usernum != -1:
    print('    ', D[usernum-1])
    usernum = int(input())
