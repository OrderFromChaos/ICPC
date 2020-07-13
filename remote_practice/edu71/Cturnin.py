Q = int(input())

for q in range(Q):
	N, A, B = [int(x) for x in input().split()]
	S = input()
	
	try:
		first1 = S.index('1')
	except ValueError:
		# No intersection pipes exist, so 1 height the entire route
		print(len(S)*(A+B) + B) # One col would be missing
		continue
	
	# Compute cost of everything before the first 1
	sumcost = (first1-1)*(A+B) + (2*A + 2*B) + B
	# Low segments + one zigzag up, and the first column on the left
	back0 = 0

	for i in range(first1, len(S)):
		s = S[i]

		if s == '0':
			back0 += 1
		else: # s == '1'	
			if back0 > 1:
				# Compute backcost only when reach a 1 after >1 0s
				lowcost = (2*A+B) + (back0-2)*(A+B) + (2*A+2*B)
				# zigzag down, low segment, zigzag up
				highcost = back0*(A+2*B)
				# always high segment

				if lowcost < highcost:
					sumcost -= (highcost - lowcost)
			back0 = 0

		sumcost += (A + 2*B) # Assume high, adjust afterward

	# Now redo backcost check since we're on endstep, except that we have to go 0 and there's no back up
	lowcost = (2*A + B) + (back0-1)*(A+B)
	# zigzag down, low segments
	highcost = back0*(A+2*B)
	# always high segment

	sumcost -= highcost - lowcost

	print(sumcost)
