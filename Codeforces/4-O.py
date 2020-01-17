import string

while True:
    order = list([str(x) for x in range(0,10)]) + list(string.ascii_uppercase)
    try:
        n = int(input())
        # print(n)
    except:
        break
    order = order[:n]
    orderset = set(order)

    state = 0
    # 0 reduc, 1 not red, 2 not latin
	
    # Check horizontal rows
    lines = []
    for L in range(n):
        line = input()
        # print(line)
        lines.append(line)
        # print(set(line) == orderset)
        if set(line) != orderset:
            state = 2
            break
    
    if state != 2:
        for L2 in range(n):
            col = [x[L2] for x in lines]
            if set(col) != orderset:
                state = 2
                break

    # Check reduced on top row
    if state != 2 and list(lines[0]) != order:
        state = 1

    # Check reduced on left column
    if state != 2 and len(lines) == n:
        if not all([x == y for x,y in zip([x[0] for x in lines], order)]):
            state = 1

    # print('    ',n, L, n-L-1)
    for i in range(0,n-L-1,1):
        _ = input() # Fix stdin
        # print('----', _)

    if state == 0:
        print('Reduced')
    elif state == 1:
        print('Not Reduced')
    else:
        print('No')