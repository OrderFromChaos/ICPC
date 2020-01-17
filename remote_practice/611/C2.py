# Algorithm
# 1. Create pool of unsure friends
# 2. Partition to non-self selections and free selections.
#    non-self means that is 5 is 0 and in the non-gift friend group,
#    then 5 is constrained to pick non-5.
#    free selections can just random select.
# 3. Select pairings for non-self first, then populate free selections

from collections import Counter, deque

N = int(input())
fi = [int(x) for x in input().split()]

freq = Counter(fi)
unsure = []
for x in range(N):
    if freq[x+1] == 0:
        unsure.append(x+1)

zeropos = set([x+1 for x in range(len(fi)) if fi[x] == 0])

# print(unsure)

nonself = [x for x in unsure if x in zeropos]
nsset = set(nonself)
nonself = deque(nonself)
free = [x for x in unsure if x not in zeropos]
fset = set(free)
free = deque(free)

# print(nonself)
# print(free)

for index, i in enumerate(fi[:-1]):
    if i != 0:
        print(i, end=' ')
    else:
        # attempt to take from nonself first. if empty, take from free
        if len(nonself) > 0:
            if len(nonself) > 1: # Won't rotate to produce itself
                if nonself[0] == index + 1:
                    nonself.rotate()
                    print(nonself.popleft(), end=' ')
                else:
                    print(nonself.popleft(), end=' ')
            else:
                if nonself[0] == index + 1:
                    print(free.popleft(), end=' ')
                else:
                    print(nonself.popleft(), end=' ')
        else:
            print(free.popleft(), end=' ')

i = fi[-1]
index = len(fi) - 1
if i != 0:
    print(i)
else:
    # attempt to take from nonself first. if empty, take from free
    if len(nonself) > 0:
        if len(nonself) > 1: # Won't rotate to produce itself
            if nonself[0] == index + 1:
                nonself.rotate()
                print(nonself.popleft())
            else:
                print(nonself.popleft())
        else:
            if nonself[0] == index + 1:
                print(free.popleft())
            else:
                print(nonself.popleft())
    else:
        print(free.popleft())
