N = int(input())
A = [int(x) for x in input().split()]

good = [4,8,15,16,23,42]
goodset = set(good)
good = {x:y for x,y in zip(good, range(len(good)))}
seqs = [0]*len(good)

remove = 0

for i in A:
    if i in goodset:
        pos = good[i]
        if pos == 0:
            seqs[pos] += 1
        else:
            if seqs[pos-1] > 0:
                seqs[pos-1] -= 1
                seqs[pos] += 1
            else:
                remove += 1
    else:
        remove += 1

mul = 1
for i in range(len(seqs)-1):
    remove += mul*seqs[i]
    mul += 1

print(remove)
