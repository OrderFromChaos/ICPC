from collections import Counter

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

Aptr = len(A)-1
Bptr = len(B)-1
p = 0
while Aptr != -1:
	if Bptr > -1:
		if A[Aptr] <= B[Bptr]:
			Bptr -= 1
		else:
			p += 1
	else:
		p += 1
	Aptr -= 1

print(p)
