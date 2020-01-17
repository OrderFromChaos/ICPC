# Check that count up (with overflow) or count down (with overflow)
# O(n)

Q = int(input())
for i in range(Q):
    N = int(input())
    students = [int(x) for x in input().split(' ')]
    fposs = True
    bposs = True
    prev = students[0]
    for i in students[1:]:
        if i - prev != 1: # c up
            if not (prev == len(students) and i == 1):
                fposs = False
        if i - prev != -1: # c down
            if not (prev == 1 and i == len(students)):
                bposs = False
        if (not fposs) and (not bposs):
            break
        prev = i
    print(['NO','YES'][any([fposs, bposs])])
