# I used a dictionary here to avoid doing int() and str() repeatedly
# instead of doing 0 <= num <= 26, but either way works.
onethru26 = set([str(x) for x in range(1,27)])
while True:
    num = int(input())
    if num == 0:
        break
    else:
        strnum = str(num)
        I = [1,1]
        if len(strnum) == 1:
            print(1)
        else:
            for char, prevchar in zip(strnum[1:],strnum):
                if prevchar + char in onethru26:
                    I.append(I[-2] + I[-1])
                else:
                    I.append(I[-1])
            print(I[-1])
