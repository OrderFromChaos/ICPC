import sys

for line in sys.stdin:
    tape = [int(x) for x in line.split(',')]

tape[1] = 12
tape[2] = 2

curr = 0
while tape[curr] != 99:
    if tape[curr] == 1:
        tape[tape[curr+3]] = tape[tape[curr+1]] + tape[tape[curr+2]]
        curr += 4
    elif tape[curr] == 2:
        tape[tape[curr+3]] = tape[tape[curr+1]] * tape[tape[curr+2]]
        curr += 4

print(tape[0])