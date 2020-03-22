N, B, A = [int(x) for x in input().split()]
S = [int(x) for x in input().split()]

# Always oom accumulator first in non-sunlight areas, then use battery
# If accumulator full in sunlight, use it regardless

b, a = B, A

for x, s in enumerate(S):
    if s == 0:
        if a > 0:
            a -= 1
        else:
            if b > 0:
                b -= 1
            else:
                print(x)
                exit(0)
    elif s == 1:
        if a == A:
            a -= 1
        else:
            if b > 0:
                b -= 1
                a = a + 1 # a guaranteed to be at most A - 1
            else:
                if a > 0:
                    a -= 1
                else:
                    print(x)
                    exit(0)
print(N)
