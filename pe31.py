combinations = [1]
coins = [1,2,5,10,20,50,100,200]

for i in range(1,10):
    ways = 0
    for coin in coins:
        if i - coin >= 0:
            ways += combinations[i - coin]
    print(ways)
    combinations.append(ways)

print(combinations[200])
