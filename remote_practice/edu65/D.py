N = int(input())
S = input()

b = [0, 0]

out = []
for c in S:
    minindex = b.index(min(b))
    maxindex = int(not minindex)
    if c == '(':
        b[minindex] += 1
        out.append(str(minindex))
    if c == ')':
        b[maxindex] -= 1
        out.append(str(maxindex))

print(''.join(out))