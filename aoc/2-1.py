import sys
from copy import deepcopy

for line in sys.stdin:
    tape = [int(x) for x in line.split(',')]

for i in range(len(tape)):
    for j in range(len(tape)):
        temp = deepcopy(tape)
        # Vary these two
        temp[1] = i
        temp[2] = j

        curr = 0
        while temp[curr] != 99:
            if temp[curr] == 1:
                temp[temp[curr+3]] = temp[temp[curr+1]] + temp[temp[curr+2]]
                curr += 4
            elif temp[curr] == 2:
                temp[temp[curr+3]] = temp[temp[curr+1]] * temp[temp[curr+2]]
                curr += 4

        if temp[0] == 19690720:
            print(100*i + j)
            exit(0)