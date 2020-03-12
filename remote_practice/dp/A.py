# Idea: added squares are (inner square - last step) + 4

bigN = int(input())

S = [1]
addval = 4

for n in range(1,101):
    S.append(S[n-1] + addval)
    addval += 4

print(S[bigN-1])
