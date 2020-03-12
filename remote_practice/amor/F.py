from collections import MutableSet

n, I = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

Ktarget = int(2 ** (int((I*8) / n) ))

# We're selecting a window, not just the most common bois

class OrderedSet():
    def __init__(self, L):
        self.m = set()
        self.elt = []
        for i in L:
            if i not in self.m:
                self.elt.append(i)
                self.m.add(i)
    def add(self, key):
        if key not in self.m:
            self.elt.append(key)

Amin = OrderedSet(A)

print(Amin.elt)

## Maximum subarray sum
#lptr = 0
#rptr = 0
#minskill = A[0]
#curr = A[0]
#maxi = A[0]
#maxcnt = 1
#while rptr != len(A) - 1:
#	if A[rptr+1] - minskill <= 5:
#		rptr += 1
#		curr += A[rptr]
#	else:
#		lptr += 1
#		if lptr >= rptr:
#			rptr += 1
#			lptr = rptr
#			minskill = A[rptr]
#			curr = A[rptr]
#		else:
#			minskill = A[lptr]
#			curr -= A[lptr-1]
#	if curr > maxi:
#		maxi = curr
#		maxcnt = rptr-lptr+1
#
#print(maxcnt)

# print(len(A) - sum(x[1] for x in Counter(A).most_common(Ktarget)))

