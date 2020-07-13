# Insight: This problem is very brute-forceable. See the n,m limits

N, M = [int(x) for x in input().split()]
mat = []
for n in range(N):
	mat.append([int(x) for x in input().split()])

# Sliding window approach
tfmat = [[(True if y == 0 else False) for y in x] for x in mat]
steps = []
for row in range(N-1):
	for col in range(M-1):
		relevant = [*mat[row][col:col+2], *mat[row+1][col:col+2]]
		if all(relevant):
			tfmat[row][col] = 1
			tfmat[row][col+1] = 1
			tfmat[row+1][col] = 1
			tfmat[row+1][col+1] = 1
			steps.append((row+1, col+1))

if all([all(x) for x in tfmat]):
	print(len(steps))
	for s in steps:
		print(*s)
else:
	print(-1)
