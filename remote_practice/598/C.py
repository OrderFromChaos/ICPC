n, m, d = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

# relative order of platforms cannot be changed, so this makes this easier
# tricky case is probably:
# 5 3 2
# 2 1 2
# here, placing on right edge is optimal. can you know in advance whether left or right edge is optimal?
# probably not, which means there's going to be a back-updating process

def printplat(L):
    global n
    fin = [0]*n
    for i, x in enumerate(L):
        l, pos = x
        fin[pos-1:(pos-1)+l] = [i+1]*l
    print(' '.join([str(x) for x in fin]))

if sum(c) > n:
    print('NO')
else:
    needed = n - sum(c) + 1
    newpos = []
    # print(needed)
    currpos = 0
    for p in [1] + c:
        # print(needed)
        newpos.append((p, currpos))
        currpos += (p-1) + max([min([needed, d]), 1])
        needed -= min([needed, d])
    lastl, lastpos = newpos[-1]
    if lastpos + (lastl-1) + d < n+1:
        print('NO')
    else:
        print('YES')
        printplat(newpos[1:])
    # if lastpos + (lastl-1) + d < n+1:
    #     print('NO')
    # else: 
    #     if lastpos + (lastl-1) <= n:
    #         print('YES')
    #         printplat(newpos)
        # else:
        #     # Rearrangement needed
        #     # We know exactly the amount of needed space, so just use that
        #     needed = n - sum(c)
        #     newpos = []
        #     # print(needed)
        #     currpos = 1
        #     for p in c:
        #         newpos.append((p, currpos))
        #         currpos += p + min([needed, d])
        #         needed -= min([needed, d])
        #         prevlen = p
        #     lastl, lastpos = newpos[-1]
        #     if lastpos + (lastl-1) > n:
        #         print('NO')
        #     else:
        #         print('YES')
        #         printplat(newpos)