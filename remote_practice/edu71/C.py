# Tradeoff
# If the cost of bourles is much less than pipe, then 2 height is optimal
# If the cost of pipe is much less than bourles, then always go down when possible (two consecutive 0s)

# Start and begin is always height 1

Q = int(input())

for q in range(Q):
	N, A, B = [int(x) for x in input().split()]
	S = input()
	
	print('------')
	print('A:', A)
	print('B:', B)

	try:
		first1 = S.index('1')
	except ValueError:
		# No intersection pipes exist, so 1 height the entire route
		print('    ', B*(len(S)+1) + A*len(S))
		for i in range(len(S)):
			print('down')
		exit(0)
	
	# Compute cost of everything before the first 1
	currcost = 2*B
	sumcost = first1*A + A + (first1)*B + 2*B
	back0 = 0

	for i in range(first1):
		print('down')

	for i in range(first1, len(S)):
		s = S[i]

		if s == '0':
			back0 += 1
		
		if s == '1' and back0 > 1:
			# Compute backcost only when reach a 1 after >1 0s
			region = back0+1
			lowcost = (region-2)*B + 4*B + (region-2)*A + 4*A
			# diff: 1A to go down, 1A to go up, B col cost during
			highcost = region*A + region*2*B
			# desc: 2B col cost during
	
			print(lowcost)
			print(highcost)

			if lowcost < highcost:
				sumcost -= (highcost - lowcost)
				for j in range(back0):
					print('down')
			else:
				for j in range(back0):
					print('up')

			currcost = 2*B
			back0 = 0
			print('up')
		elif s == '1':
			# Must be 1 with back0 <= 1
			print('up')
			back0 = 0

		sumcost += currcost + A

	# Now redo backcost check since we're on endstep, except that we have to go 0 and there's no back up
	lowcost = back0*B + back0*A + A
	# diff: 1A to go down, B col cost during
	highcost = back0*A + back0*2*B
	# desc: 2B col cost during

	print('Force step')
	print('back0:', back0)
	print(lowcost)
	print(highcost)

	sumcost -= (highcost - lowcost)

	for i in range(back0):
		print('down')

	print('    ', sumcost)
