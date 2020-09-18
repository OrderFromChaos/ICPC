T = int(input())

for t in range(T):
    n, k = [int(x) for x in input().split()]
    s = list(input())

    # Strategy: search until you reach a forcing window, then
    #  propagate that throughout the bitstring
    # Sliding window: throw out the left bit count, update right. Saves time

    # hypothesis: if possible, you should be able to greedy construct the bitstring
    meta = [] # stores window info
    
    # Do first window
    f0, f1 = 0, 0
    q = []
    for i in range(k):
        c = s[i]
        if c == '0':
            f0 += 1
        elif c == '1':
            f1 += 1
        else:
            q.append(i)
    # Check for forcing
    if f0 != f1 and abs(f1-f0) == len(q):
        if f0 < f1: # too many 1s
            for i in q:
                s[i] = '0'
            f0 = f1
        else:       # too many 0s
            for i in q:
                s[i] = '1'
            f1 = f0
    meta.append([f0, f1, q])
    
    # Sliding window
    for end in range(k, len(s)):
        cm = meta[end-k]

