T = int(input())

for i in range(T):
    lastlen = 0
    X = int(input())
    S = [int(x) for x in input()]
    # Only need to store string up to length X
    length = len(S)
    S = S + [0]*(X-len(S))
    lastlen = length
    l = 0
    # print('---', X, S, '---')
    while l != X + 1:
        # print(''.join(map(str, S)), length)
        lastlen = length
        l += 1
        cutlen = length - l
        if length >= X + 1:
            # No need to append; already covered all S[l] calls
            length = l + cutlen * S[l - 1]
        else:
            # Have to append
            base = S[l:length]
            if base:
                stuff = base * S[l - 1]
                # print('   ', ''.join(map(str,stuff)))
                if l + len(stuff) > X + 1:
                    # print('too long')
                    S[l:X] = stuff[:X - len(stuff) - l + 1]
                else:
                    S[l:l+len(stuff)] = stuff 
                length = l + cutlen * S[l - 1]
    print(lastlen%(1000000000 + 7))