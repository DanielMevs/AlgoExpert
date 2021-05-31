#Given an array of arrays where each subarray holds two integer values
#and represents an item.
#The first integer is the item's value and the second integer is the item's weight.
#You're also given an integer representing the maximum capacity of a knapsack you have
#Write a function that returns the maximized combined value of the items that you should 
#pick as well as an array of the indices of each item picked.

#O(nc) time | O(nc) space
def knapsackProblem(items, capacity):
    knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
    	currentWeight = items[i - 1][1]#minus one because we are keeping in account empty items
    	currentValue = items[i - 1][0]
    	for c in range(0, capacity + 1):
    		if currentWeight > c:
    			knapsackValues[i][c] = knapsackValues[i - 1][c]
    		else:
    			knapsackValues[i][c] = max(knapsackValues[i - 1][c], knapsackValues[i-1][c - currentWeight] + currentValue)
    return [knapsackValues[-1][-1], getKnapSackItems(knapsackValues, items)]

def getKnapSackItems(knapsackValues, items):
	sequence = []
	i = len(knapsackValues) - 1
	c = len(knapsackValues[0]) - 1
	while i > 0:
		if knapsackValues[i][c] == knapsackValues[i - 1][c]:
			i -= 1 
		else:
			sequence.append(i - 1)
			c -= items[i - 1][1]
			i -= 1
		if c == 0:
			break

	return list(reversed(sequence))
