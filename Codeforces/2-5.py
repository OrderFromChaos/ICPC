# This problem is ranked *2300 ELO! Very hard for competition.

# General idea:
# We want to where the sequence the requested index is in starts. This will make finding the number
#     fairly straightforward.
# To do this, here are the general algorithm steps:
# 1. The length of the entire string needs to be split into buckets - 1->9 are of length 1,
#        10->99 are of length 2, etc.
#    Note that the length of some large N subsequence is going to be {\sum}_{k=1}^{9}k + {\sum}_{k=10}^{99}2k + ...
#    Generally, this is C * {\sum}_{k=s}^{n}k , where C is some constant. Knowing the closed form of
#    this sum is the "magic" mathematical insight needed, which can be found on WolframAlpha:
#    {\sum}_{k=s}^{n}k == (n-s+1)(n+s)/2
#    Once we have this, the rest isn't quite as bad.
#    First, generate the constant terms leading up to new length sequences:
#        {\sum}_{k=1}^{9}  k = 45
#    2 * {\sum}_{k=10}^{99}k = 9810
#    ...
# 2. Now with each new index, find the nearest smallest position in the list above (should only be like 18 entries),
#        so linear search is fine.
#    Let's say the index is 10000, it's in the 3-length sequence range and is preceeded by 9810 chars from the
#        2 and 1 length sequences.
# 3. Generate the relevant sum for said sequence. In this case, it's {\sum}_{k=100}^{n}3k = 3*(n-99)(n+100)/2.
#        Do binary search over the input n to the sum. Our space of possibilities is 10**19, so this is like
#        60 ops in the worst case.
# 4. Once you have the input n, do index - f(n) - const. term. This should equal the number.

from bisect import bisect_left

class BinSearchFxn:
    def __init__(self):
        self.fxn = lambda n: n*(n+1)//2
        self.uppbound = 10**18
    def __getitem__(self,i):
        return self.fxn(i)
    def __len__(self):
        return self.uppbound

a = BinSearchFxn()
insertion = bisect_left(a, 10**15)
print(insertion)
