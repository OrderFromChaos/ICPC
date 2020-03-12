from bisect import bisect_left

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

ra = [0]
roomcount = 0
for i in A:
	roomcount += i
	ra.append(roomcount)

for i in B:
	index = bisect_left(ra, i)
	if i != 0:
		index -= 1
	room = i - ra[index]
	print(index+1, room)

