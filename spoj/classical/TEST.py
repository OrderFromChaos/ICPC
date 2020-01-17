import sys

i = []
for line in sys.stdin:
    if line != '42\n':
        i.append(line.strip())
    else:
        break

for j in i:
    print(j)
