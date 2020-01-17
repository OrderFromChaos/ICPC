# 0 if all A
# 1 if edge full A
# 2 if one A corner
# 3 if edge A, but not corner
# 4 if no A on edge
# MORTAL if no A


from collections import Counter

cases = int(input())
for cas in range(cases):
    r, c = [int(x) for x in input().split(' ')]
    data = [input() for x in range(r)]
    lc, rc = zip(*[(x[0], x[c-1]) for x in data])
    edges = [data[0], data[r-1], lc, rc]
    freqs = [Counter(x) for x in edges]
    allfreq = [Counter(x) for x in data]
    # print(freqs)
    if all([x['A'] == c for x in allfreq]):
        print(0)
    else:
        if freqs[0]['A'] == c or freqs[1]['A'] == c or freqs[2]['A'] == r or freqs[2]['A'] == r:
            print(1)
        else:
            if 'A' in [data[0][0], data[0][c-1], data[r-1][0], data[r-1][c-1]]:
                print(2)
            else:
                if any([x['A'] > 0 for x in freqs]):
                    print(3)
                else:
                    # Check for ANY a
                    if any([x['A'] > 0 for x in allfreq]):
                        print(4)
                    else:
                        print('MORTAL')
