import heapq

Q = int(input())

for q in range(Q):
    n, k = [int(x) for x in input().split()]
    s = input()

    # zeropos should be a maxheap
    # onepos should be a minheap
    # reason: want to insert in sorted order
    # if zeropos top is less than onepos top, then bin string is sorted and can stop

    zeropos = []
    onepos = []

    for i, x in enumerate(s):
        if x == '0':
            zeropos.append(-i) # to force maxheap
        else:
            onepos.append(i)
    
    heapq.heapify(zeropos)
    heapq.heapify(onepos)
    
    # When swapping
    # Remove zeroes from the end, remove ones from the front
    for i in range(k):
        if -zeropos[0] < onepos[0]:
            # list is sorted
            break
        else:
            zpos = heapq.heappop(zeropos)
            opos = heapq.heappop(onepos)
            heapq.heappush(zeropos, -opos)
            heapq.heappush(onepos,  -zpos)

    # Sort complete, now just output the binary string

    zeropos = [x*-1 for x in zeropos]
    heapq.heapify(zeropos)

    print('zero', zeropos)
    print('one', onepos)
    print()

    finstr = []
    for i in range(n):
        if len(zeropos) > 0 and len(onepos) > 0:
            if zeropos[0] < onepos[0]:
                finstr.append('0')
                heapq.heappop(zeropos)
            else:
                finstr.append('1')
                heapq.heappop(onepos)
        elif len(onepos) > 0:
            finstr += ['1']*len(onepos)
            break
        elif len(zeropos) > 0:
            finstr += ['0']*len(zeropos)
            break
    print(''.join(finstr))