#O(nd) time | O(n) space
def numberOfWaysToMakeChange(n, denoms):
	ways = [0 for amount in range(n+1)]
	ways[0] = 1 #will serve as base case
	for denom in denoms:
		for amount in range(1, n+1):
			if denom <= amount:
				ways[amount] += ways[amount - denom]
				#ways[amount] = ways[amount] + way[amount-denom]
	return ways[n]