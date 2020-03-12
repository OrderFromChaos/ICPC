import bisect

# I'm not really sure how to make this nlogn.

L = [6, 2, 5, 1, 7, 4, 8, 3]
A = [1]
previous = [6]

for i in range(1, len(L)):
    largest = bisect.bisect_left(previous, L[i])
    
