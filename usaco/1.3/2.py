"""
ID: sourcef3
LANG: PYTHON3
TASK: transform
"""

problemname = 'transform'

with open(problemname + '.in','r') as f:
    data = [x.strip() for x in f.readlines()]

N = int(data[0])
original = data[1:N+1]
trans = data[N+1:]

def rotate_90(pattern):
    # clockwise
    N = len(pattern)
    new = [['']*N]*N
    for i, x in enumerate(new):
        for j in range(N):
            x[j] = pattern[N-j-1][i]
        new[i] = ''.join(new[i])
    return new

def reflect(pattern):
    return [x[::-1] for x in pattern]

# print(original)
# print(trans)

valid = []

mat90 = rotate_90(original)
mat180 = rotate_90(mat90)
mat270 = rotate_90(mat180)
refl = reflect(original)
refl90 = rotate_90(refl)
refl180 = rotate_90(refl90)
refl270 = rotate_90(refl180)

if trans == mat90:
    valid.append(1)
if trans == mat180:
    valid.append(2)
if trans == mat270:
    valid.append(3)
if trans == refl:
    valid.append(4)
if trans in [refl90, refl180, refl270]:
    valid.append(5)
if trans == original:
    valid.append(6)

if not valid:
    valid.append(7)

with open(problemname + '.out','w') as f:
    f.write(str(min(valid)))
    f.write('\n')