# Use a queue, store all starts encountered while adding to previous elements

S = input()
T = input()
Tl = set(T)

substr = []
# format: [[(char, Spos, Tpos), ...], [...], ...]
for i in S:
    if i in Tl:
        