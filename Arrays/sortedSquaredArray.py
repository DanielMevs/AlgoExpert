def sortedSquaredArray(array):
	squaredArray = [0 for _ in array]
    smallerValueIdx = 0
	largerValueIdx = len(array) -1
	
	for idx in reversed(range(len(array))):
		smallerValue =array[smallerValueIdx]
		largerValue = array[largerValueIdx]
		
		if abs(smallerValue) > abs(largerValue):
			squaredArray[idx] = smallerValue * smallerValue
			smallerValueIdx += 1
		else:
			squaredArray[idx] = largerValue * largerValue
			largerValueIdx -= 1
		
    return squaredArray
