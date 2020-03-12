from collections import deque

N = int(input())
C = deque([int(x) for x in input().split()])

scores = [0,0,0]
state = 1
while C:
	if C[0] > C[-1]:
		scores[state] += C.popleft()
	else:
		scores[state] += C.pop()
	state *= -1
#	some not useful code
#	to comment out

print(scores[1], scores[-1])
