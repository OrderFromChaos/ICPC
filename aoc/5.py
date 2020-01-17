import sys
from time import sleep

ID = 5

for line in sys.stdin:
    tape = [int(x) for x in line.split(',')]

curr = 0
while curr < len(tape):
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
        99: '[break]'
    }
    print(keys[opcode] if opcode in keys else opcode, modecode, tape[curr:curr+(4 if opcode < 3 else 2)])

    # TODO: Adjust statements for opcode 1 and 2
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
        inputval = ID
        tape[tape[curr+1]] = inputval
        curr += 2
    elif opcode == 4:
        print('---', tape[tape[curr+1]], '---')
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
        break
    else:
        raise Exception('Invalid opcode:', opcode)

    if opcode not in [5,6] and (startinst != tape[startcurr]):
        curr = startcurr
