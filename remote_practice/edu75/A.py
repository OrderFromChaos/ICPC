# from string import ascii_lowercase as al

T = int(input())
for t in range(T):
	S = input()
	last = ';'
	popped = False
	valid = []
# 	print(valid)
	for s in S:
		if s != last:
			popped = False
			valid.append(s)
		else:
			if not popped:
				popped = True
				valid.pop()
		last = s
# 		print(valid)
	print(''.join(sorted(list(set(valid)))))
