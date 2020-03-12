from collections import Counter

_ = input()
A = [int(x) for x in input().split()]

bad = set(x for x, y in Counter(A).items() if y > 1)

removed = Counter()

for i, x in enumerate(A):




# Want to select the best rightmost and leftmost edges of subelement arrays.
# For example, in 1 4 1 4 9,
# We want to take away the rightmost 1 and either the left or rightmost 4.
# In 1 1 2 2,
# We want to take away the rightmost 1 and the leftmost 2.

for i, x in enumerate(A):
	if x in seen:
		if leftmostbad == -1:
			leftmostbad = i
		rightmostbad = i
	else:
		seen.add(x)

if leftmostbad != -1:
	print(rightmostbad-leftmostbad+1)
else:
	print(0)
