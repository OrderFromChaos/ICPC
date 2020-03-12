
def fib(n):
    a = 1
    b = 1
    yield a
    yield b

    for i in range(n-2):
        c = a + b
        a = b
        b = c
        yield c

print(fib(10))
print(list(fib(10)))