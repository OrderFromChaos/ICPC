Q = int(input())
for q in range(Q):
    N, K = [int(x) for x in input().split()]
    # Theory: only the game <= k + 2 matters
    # Without k, Bob wins start % 3 == 0
    if N < K:
        if N % 3 == 0:
            print('Bob')
        else:
            print('Alice')
    else:
        # Just generate the list
        state = []
        # print(N, K)
        for i in range(K):
            # 0 = Bob
            state.append(i % 3 != 0)
        # print(state)
        for i in range(K, N+1):
            if False in [state[-1], state[-2], state[-K]]:
                state.append(True)
            else:
                state.append(False)
        # print(state)
        print(['Bob','Alice'][state[N]])
