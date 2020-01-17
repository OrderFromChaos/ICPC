from bisect import bisect_left
from math import ceil

x = int(input())
n = x - 1
s = 1
middle = (n - s + 1)*(s+n)/4
# print(middle)
middle = ceil(middle)

class BinSearchFxn:
	def __init__(self):
		self.fxn = lambda n: (n)*(n+1)//2
		self.uppbound = 1000000009
	def __getitem__(self, i):
		return self.fxn(i)
	def __len__(self):
		return self.uppbound

a = BinSearchFxn()
prev = bisect_left(a, middle)
if a[prev] == middle:
    prev += 1

if n == 1: # Fails for this case, works for all others
	print(1)
else:
	print(n-prev+1)