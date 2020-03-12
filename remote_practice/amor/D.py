_ = input()
A = [int(x) for x in input().split()]
A.sort()

# Maximum subarray sum
lptr = 0
rptr = 0
minskill = A[0]
curr = A[0]
maxcnt = 1
while rptr != len(A) - 1:
	if A[rptr+1] - minskill <= 5: 		# If you can add more team members, do it!
		rptr += 1
	else:						  		# Otherwise throw out old team members.
		lptr += 1
		if lptr >= rptr:				# Check if there are no team members, and if so, skip ahead to having one team member.
			rptr += 1
			lptr = rptr
			minskill = A[rptr]
		else:							# If there are still team members, reset minskill to be leftmost and curr to be curr -= A[lptr-1].
			minskill = A[lptr]
	count = rptr - lptr + 1
	if count > maxcnt:
		maxcnt = count

print(maxcnt)
