memo = {0: 1,
        1: 1}
def fib(n): # Makes next fibonacci number in seq.
            # Stores all along the way so as to reduce subproblems
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

fib(100)
print(list(memo.values()))
