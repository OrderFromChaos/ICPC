from collections import Counter

# Note: friend cannot give to self

N = int(input())
fi = [int(x) for x in input().split()]

freq = Counter(fi)
who = [freq[x+1] for x in range(N)]
zeropos = who.index(0)
# print(who)
# print(fi)
# print(zeropos)

for index, i in enumerate(fi[:-1]):
    if i != 0:
        print(i, end=' ')
    else:
        # Check that zeropos isn't self
        if zeropos == index:
            old = zeropos
            zeropos += 1
            while zeropos < len(fi) and who[zeropos] != 0:
                zeropos += 1
            who[zeropos] = 1
            print(zeropos+1, end=' ')
            zeropos = old
        else:
            print(zeropos+1, end=' ')
            # update zeropos (to make O(N) and not O(N^2))
            zeropos += 1
            while zeropos < len(fi) and who[zeropos] != 0:
                zeropos += 1

i = fi[-1]
if i != 0:
    print(i)
else:
    print(zeropos+1)
