V, P = input().split(' ')
locs = input().split(' ')

distances = [[]]*V

for v1 in locs:
    temp = []
    for v2 in locs:
        temp.append(v2-v1)
    
