from collections import deque
from collections import Counter

# Gonna steal this from https://cses.fi/book/book.pdf "Edit Distance"

Q = int(input())
for q in range(Q):
    S = deque(input())
    T = deque(input())
    Pfreq = Counter(input())

    while len(T) > 0:
        if len(S) and S[0] == T[0]:
            S.popleft()
            T.popleft()
        else:
            if Pfreq[T[0]] > 0:
                Pfreq[T[0]] -= 1
                T.popleft()
            else:
                break

    if len(S) == 0 and len(T) == 0:
        print('YES')
    else:
        print('NO')

# This is probably actually DP - you want to insert from P so S maximally matches T