import re

N = int(input())
numbers = []

# This is a stupidly sadistic input format
findnums = re.compile(r"-?\d+")
while True:
    numbers += [int(x) for x in findnums.findall(input())]
    if len(numbers) == N*N:
        break

# Define how to access the matrix
def getEntries(rS,rE,cS,cE): # row Start, row End, column Start, column End
    # Indexing starts at 0
    if rS == rE:
        start = rS*N
        return numbers[start+cS : start+cE]
    else:
        temp = []
        for row in range(rS,rE):
            start = row*N
            temp += numbers[start+cS : start+cE]
        return temp

# Idea: Some rows and columns have net negative utility. It is strictly worse to keep these rows and columns.
# Start by assuming the entire N*N matrix is your maximum subrectangle, then remove parts that you don't want to keep.
dims = (0,N-1,0,N-1)

linesizeRC = [1,1]
while True: # backcounter loop
    STARTR, ENDR, STARTC, ENDC = dims
    print(dims,linesizeRC)
    changedR = False
    changedC = False
    sizeR, sizeC = (ENDR-STARTR,ENDC-STARTC)

    # top
    if sum(getEntries(STARTR,STARTR+linesizeRC[0],STARTC,ENDC)) <= 0:
        dims = (STARTR + linesizeRC[0], ENDR, STARTC, ENDC)
        changedR = True
    # bottom
    elif sum(getEntries(ENDR-linesizeRC[0],ENDR, STARTC,ENDC)) <= 0:
        dims = (STARTR, ENDR-linesizeRC[0], STARTC, ENDC)
        changedR = True

    # left
    if sum(getEntries(STARTR,ENDR,STARTC,STARTC + linesizeRC[1])) <= 0:
        dims = (STARTR, ENDR, STARTC+linesizeRC[1], ENDC)
        changedC = True
    # right
    elif sum(getEntries(STARTR,ENDR,ENDC-linesizeRC[1],ENDC)) <= 0:
        dims = (STARTR, ENDR, STARTC, ENDC-linesizeRC[1])
        changedC = True


    if linesizeRC == [sizeR, sizeC]:
        break

    if changedR:
        linesizeRC[0] = 1
    else:
        linesizeRC[0] = linesizeRC[0] + 1

    if changedC:
        linesizeRC[1] = 1
    else:
        linesizeRC[1] = linesizeRC[1] + 1


# Compute sum of region
print(sum(getEntries(*dims)))
