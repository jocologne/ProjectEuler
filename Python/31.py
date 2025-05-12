coins = [1, 2, 5, 10, 20, 50, 100, 200]

def count_ways_to_make_change(target, coins):
	ways = [0] * (target + 1)
	ways[0] = 1
	for coin in coins:
		for amount in range(coin, target + 1):
			ways[amount] += ways[amount - coin]
	return ways[target]

print(count_ways_to_make_change(200, coins))