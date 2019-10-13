import re
import numpy as np

N = int(input())
numbers = []

# This is a stupidly sadistic input format
findnums = re.compile(r"-?\d+")
while True:
    numbers += [int(x) for x in findnums.findall(input())]
    if len(numbers) == N*N:
        break

arr = np.array([numbers[x:x+N] for x in range(0,len(numbers),N)])
print(arr)

# Idea: Some rows and columns have net negative utility. It is strictly worse to keep these rows and columns.
# Start by assuming the entire N*N matrix is your maximum subrectangle, then remove parts that you don't want to keep.

sumboth = lambda arr: np.sum(np.sum(arr,axis=1),axis=0)

sizeX = 0
sizeY = 0
sizereduce = False
while True:
    if sizereduce:
        sizeX = 1
        sizeY = 1
        sizereduce = False
    else:
        sizeX += 1
        sizeY += 1
        if sizeX > arr.shape[0] and sizeY > arr.shape[1]: # Termination condition
            break

    potential_arrs = []
    if sizeY < arr.shape[0] and sumboth(arr[:sizeY,:]) < 0: # check top
        newarr = arr[sizeY:,:]
        potential_arrs.append((newarr,sumboth(newarr)))
        sizereduce = True
    if sizeY < arr.shape[0] and sumboth(arr[-sizeY:,:]) < 0: # check bottom
        newarr = arr[:-sizeY,:]
        potential_arrs.append((newarr,sumboth(newarr)))
        sizereduce = True
    if sizeX < arr.shape[1] and sumboth(arr[:,:sizeX]) < 0: # check left
        newarr = arr[:,sizeX:]
        potential_arrs.append((newarr,sumboth(newarr)))
        sizereduce = True
    elif sizeX < arr.shape[1] and sumboth(arr[:,-sizeX:]) < 0: # check right
        newarr = arr[:,:-sizeX]
        potential_arrs.append((newarr,sumboth(newarr)))
        sizereduce = True

    if sizereduce:
        maximum = 0
        maxindex = 0
        for i, arr_group in enumerate(potential_arrs):
            sumval = arr_group[1]
            if sumval > maximum:
                maximum = sumval
                maxindex = i
        arr = potential_arrs[maxindex][0]

    print()
    print(arr)

print(sumboth(arr))
