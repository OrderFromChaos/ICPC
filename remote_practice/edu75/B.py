from collections import Counter

Q = int(input())
for q in range(Q):
	N = int(input())
	zeros, ones = 0, 0
	lengths = []
	for n in range(N):
		S = input()
		lengths.append(len(S))
		freq = Counter(S)
		zeros += freq['0']
		ones += freq['1']
	# Greedy select max 1s
	avail = 0
	# Can be taken out as 1 from odd, then 2
	# 2 always from even
	for l in lengths:
		if l % 2 == 0:
			oo = ones
			ones -= min([l, (ones//2)*2])
			avail = oo - ones
		else:
			oo = ones
			if ones % 2 == 0:
				if ones > 0:
					ones -= min([l, ones-1])
			else:
				ones -= min([l, ones])
			avail 
	if ones > 0:
		print(N-1)
	else:
		print(N)


