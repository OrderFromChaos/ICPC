A = [5,6,4,9,2]

nums = (*sorted( [(x,y) for x,y in zip(A, range(len(A)))] ))
print(A)
print(nums)
