import sys
from time import sleep

ID = 1

for line in sys.stdin:
    tape = [int(x) for x in line.split(',')]

def grabmode(x, mode):
    global tape
    global relbase
    if mode == '0': # position mode
        print(f'    Returning value {mode}', tape[tape[x]])
        print('   ', tape[x])
        return tape[tape[x]]
    elif mode == '1': # immediate mode
        print(f'    Returning value {mode}', tape[x])
        return tape[x]
    elif mode == '2': # relative mode
        term = tape[x]+relbase
        if term > 0:
            print(f'    Returning value {mode}', tape[relbase])
            return tape[term]
        else:
            print(f'    Returning value {mode}', tape[0])
            return tape[0]
    else:
        raise Exception('Unrecognized mode!', mode)

tape += [0]*1000

curr = 0
relbase = 0
while True:
    # Step 1: Grab modecodes
    # Step 2: Run statement with modecodes
    stmt = str(tape[curr])
    opcode = int(stmt[-2:])
    startcurr = curr
    startinst = tape[curr]

    modecode = stmt[:-2][::-1]
    if len(modecode) < 2:
        modecode += '0'*(2-len(modecode))
    keys = {
        1: '[+]',
        2: '[*]',
        3: '[input]',
        4: '[diag]',
        5: '[JNZ]',
        6: '[JEZ]',
        7: '[<]',
        8: '[==]',
        9: '[+-rel]',
        99: '[break]'
    }
    print(keys[opcode] if opcode in keys else opcode, modecode, tape[curr:curr+4], relbase)

    if opcode == 1:
        # eg [1, 3, 2, 5] -> tape[5] = tape[2] + tape[3]
        tape[tape[curr+3]] = grabmode(curr+1, modecode[0]) + grabmode(curr+2, modecode[1])
        curr += 4

    elif opcode == 2:
        # eg [1, 3, 2, 5] -> tape[5] = tape[2] * tape[3]
        tape[tape[curr+3]] = grabmode(curr+1, modecode[0]) * grabmode(curr+2, modecode[1])
        curr += 4

    elif opcode == 3:
        inputval = ID
        tape[tape[curr+1]] = inputval
        curr += 2
    elif opcode == 4:
        print('---', grabmode(curr+1, modecode[0]), '---')
        curr += 2
    elif opcode == 5:
        # JNZ: [5, 1, 2]
        checkval = grabmode(curr+1, modecode[0])
        
        if checkval != 0:
            curr = grabmode(curr+2, modecode[1])
        else:
            curr += 3
    elif opcode == 6:
        # JEZ
        checkval = grabmode(curr+1, modecode[0])
        
        if checkval == 0:
            curr = grabmode(curr+2, modecode[1])
        else:
            curr += 3
    elif opcode == 7:
        # <
        first = grabmode(curr+1, modecode[0])
        second = grabmode(curr+2, modecode[1])
        tape[tape[curr+3]] = (first < second)

        curr += 4
    elif opcode == 8:
        # ==
        first = grabmode(curr+1, modecode[0])
        second = grabmode(curr+1, modecode[1])
        tape[tape[curr+3]] = (first == second)
        
        curr += 4
    elif opcode == 9:
        # change relbase
        relbase += grabmode(curr+1, modecode[0])
        curr += 2
    elif opcode == 99:
        break
    else:
        raise Exception('Invalid opcode:', opcode)

    if opcode not in [5,6] and (startinst != tape[startcurr]):
        curr = startcurr