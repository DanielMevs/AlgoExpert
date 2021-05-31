#O(n) time | O(n) space
def maxSubsetSumNoAdjacent1(array):
	if not len(array):
		return 0
	elif len(array) == 1:
		return array[0] 
	maxSums = array[:] #maxSum[0] = array[0]
	for i in range(2, len(array)):
		maxSum[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
		
	return maxSums[-1]
	
#O(n) time | O(1) space => more optimal
def maxSubsetSumNoAdjacent2(array):
	if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]
	second = array[0]
	first = max(array[0], array[1])
	for i in range(2, len(array)):
		current = max(first, second+array[i])
		second = first
		first = current
	return first
	