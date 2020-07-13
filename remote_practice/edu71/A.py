Q = int(input())
for q in range(Q):
	B, P, F = [int(x) for x in input().split()]
	H, C = [int(x) for x in input().split()]

	profit = 0

	if H > C:
		# Sell hamburgers first
		hams = min([B//2, P])
		B -= hams*2
		P -= hams
		profit += H * hams
		
		# Pick up remainder
		if B > 0:
			chicks = min([B//2, F])
			B -= chicks*2
			F -= chicks
			profit += C * chicks
	else:
		# Sell chicken sandwiches first
		chicks = min([B//2, F])
		B -= chicks*2
		F -= chicks
		profit += C * chicks
	
		# Pick up remainder
		if B > 0:
			hams = min([B//2, P])
			B -= hams*2
			P -= hams
			profit += H * hams
	
	print(profit)




