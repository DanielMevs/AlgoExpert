#O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumIdx = 0
    for i in range(len(array)):
    	print("i: ", i)
    	currentNum = array[i]
    	print("currentNum", currentNum)
    	for j in range(0, i):
    		print("j: ", j)
    		otherNum = array[j]
    		print("otherNum: ", otherNum)
    		if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
    			sums[i] = sums[j] + currentNum
    			print("sums: ", sums)
    			sequences[i] = j
    			print("sequences: ", sequences)
    	if sums[i] >= sums[maxSumIdx]:
    		maxSumIdx = i
    	print("\n")
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]

def buildSequence(array, sequences, currentIdx):
	sequence = []
	while currentIdx is not None:
		sequence.append(array[currentIdx])
		currentIdx = sequences[currentIdx]
	return list(reversed(sequence))



array = [10, 70, 20, 30, 50, 11, 30]
maxSumIncreasingSubsequence(array)