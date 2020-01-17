N = int(input())
chips = [int(x) for x in input().split(' ')]

odds = sum([i%2 for i in chips])
evens = sum([i%2 == 0 for i in chips])

if odds >= evens:
    print(evens)
else:
    print(odds)