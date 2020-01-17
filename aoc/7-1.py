import sys
from time import sleep
from itertools import permutations, cycle
from copy import deepcopy

inval = [5,6,7,8,9]

for line in sys.stdin:
    tapeorigin = [int(x) for x in line.split(',')]

# TODO FIXME: Do feedback loop system (while loop)
# Still requires permutations

outputs = []
for p in permutations(inval):
    signal = 0
    amptape = [deepcopy(tapeorigin) for i in range(5)]
    gotval = [False]*5
    for index, i in enumerate(cycle(p)):
        curr = 0
        tape = amptape[index%5]
        print(index, i)
        while curr < len(tape):
            # Step 1: Grab modecodes
            # Step 2: Run statement with modecodes
            stmt = str(tape[curr])
            opcode = int(stmt[-2:])
            startcurr = curr
            startinst = tape[curr]
            breakcode = 90

            modecode = stmt[:-2][::-1]
            if len(modecode) < 2:
                modecode += '0'*(2-len(modecode))
            keys = {
                1: '[+]',
                2: '[*]',
                3: '[input]',
                4: '[signal]',
                5: '[JNZ]',
                6: '[JEZ]',
                7: '[<]',
                8: '[==]',
                99: '[break]'
            }
            print(keys[opcode] if opcode in keys else opcode, modecode, tape[curr:curr+(4 if opcode < 3 else 2)])

            if opcode == 1:
                # eg [1, 3, 2, 5] -> tape[5] = tape[2] + tape[3]
                if modecode[0] == '0':
                    oldval = tape[tape[curr+3]]
                    if modecode[1] == '0':
                        tape[tape[curr+3]] = tape[tape[curr+1]] + tape[tape[curr+2]]
                    elif modecode[1] == '1':
                        tape[tape[curr+3]] = tape[tape[curr+1]] + tape[curr+2]
                elif modecode[0] == '1':
                    if modecode[1] == '0':
                        tape[tape[curr+3]] = tape[curr+1] + tape[tape[curr+2]]
                    elif modecode[1] == '1':
                        tape[tape[curr+3]] = tape[curr+1] + tape[curr+2]
                # print('+ op: Old: {}, New: {}'.format(oldval, tape[tape[curr+3]]))
                curr += 4

            elif opcode == 2:
                # eg [1, 3, 2, 5] -> tape[5] = tape[2] * tape[3]
                if modecode[0] == '0':
                    if modecode[1] == '0':
                        tape[tape[curr+3]] = tape[tape[curr+1]] * tape[tape[curr+2]]
                    elif modecode[1] == '1':
                        tape[tape[curr+3]] = tape[tape[curr+1]] * tape[curr+2]
                elif modecode[0] == '1':
                    if modecode[1] == '0':
                        tape[tape[curr+3]] = tape[curr+1] * tape[tape[curr+2]]
                    elif modecode[1] == '1':
                        tape[tape[curr+3]] = tape[curr+1] * tape[curr+2]
                curr += 4

            elif opcode == 3:
                if not gotval[index%5]:
                    gotval[index%5] == True
                    inputval = i
                else:
                    inputval = signal
                tape[tape[curr+1]] = inputval
                curr += 2
            elif opcode == 4:
                # print('---', tape[tape[curr+1]], '---')
                signal = tape[tape[curr+1]]

                curr += 2
            elif opcode == 5:
                # JNZ: [5, 1, 2]
                if modecode[0] == '0':
                    checkval = tape[tape[curr+1]]
                elif modecode[0] == '1':
                    checkval = tape[curr+1]
                
                if checkval != 0:
                    if modecode[1] == '0':
                        curr = tape[tape[curr+2]]
                    elif modecode[1] == '1':
                        curr = tape[curr+2]
                else:
                    curr += 3
            elif opcode == 6:
                # JEZ
                if modecode[0] == '0':
                    checkval = tape[tape[curr+1]]
                elif modecode[0] == '1':
                    checkval = tape[curr+1]
                
                if checkval == 0:
                    if modecode[1] == '0':
                        curr = tape[tape[curr+2]]
                    elif modecode[1] == '1':
                        curr = tape[curr+2]
                else:
                    curr += 3
            elif opcode == 7:
                # <
                if modecode[0] == '1':
                    first = tape[curr+1]
                elif modecode[0] == '0':
                    first = tape[tape[curr+1]]
                if modecode[1] == '1':
                    second = tape[curr+2]
                elif modecode[1] == '0':
                    second = tape[tape[curr+2]]

                if first < second:
                    boolval = 1
                else:
                    boolval = 0
                tape[tape[curr+3]] = boolval

                curr += 4
            elif opcode == 8:
                # ==
                if modecode[0] == '1':
                    first = tape[curr+1]
                elif modecode[0] == '0':
                    first = tape[tape[curr+1]]
                if modecode[1] == '1':
                    second = tape[curr+2]
                elif modecode[1] == '0':
                    second = tape[tape[curr+2]]

                if first == second:
                    boolval = 1
                else:
                    boolval = 0
                tape[tape[curr+3]] = boolval
                
                curr += 4
            elif opcode == 99:
                breakcode = 99
                break
            else:
                raise Exception('Invalid opcode:', opcode)

            if opcode not in [5,6] and (startinst != tape[startcurr]):
                curr = startcurr
            
            if index % 5 == 0:
                outputs.append(signal)
        amptape[index%5] = tape
        if breakcode == 99:
            break
    print('#### Finished after', index,'amps ####')

# print(outputs)
print(max(outputs))