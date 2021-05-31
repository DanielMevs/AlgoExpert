#Write a function that takes in an integer matrix of potentially unequal height and width and returns the minimum
#number of passes required to convert all negative integers in the matrix to positive integers.
#A negative integer in the matrix can only be converted to a positive integer if one or more of its
#adjacent elements is positive.
#An adjacent element is an element that is to the left, to the right, above, or below the current element in the matrix. 
#Note that the 0 value is neither positive nor negative, meaning that a 0 can't convert an adjacent negative to positve.

def minimumPassesOfMatrix(matrix):
    passes = convertNegatives(matrix)
    return passes - 1 if not containsNegative(matrix) else -1

def convertNegatives(matrix):
	nextPassQueue = getAllPositivePositions(matrix)
	passes = 0

	while len(nextPassQueue) > 0:
		currentPassQueue = nextPassQueue
		nextPassQueue = []

		while len(currentPassQueue) > 0:
			#O(n) operation in Python
			#To make O(1) operation, we could use the `deque` object.
			#For our time complexity analysis, we'll assume this runs in O(1) time.
			#We could also turn this queue into a stack and replace `.pop(0) with the
			#constant-time `.pop()` operation
			currentRow, currentCol = currentPassQueue.pop(0)

			adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix)
			for position in adjacentPositions:
				row, col = position
				value = matrix[row][col]
				if value < 0:
					matrix[row][col] *= -1
					nextPassQueue.append([row, col])
		passes += 1

	return passes

def getAllPositivePositions(matrix):
	positivePositions = []

	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			value = matrix[row][col]
			if value > 0:
				positivePositions.append([row, col])

	return positivePositions


def getAdjacentPositions(row, col, matrix):
	adjacentPositions = []

	#check if there is a neighbor above us
	if row > 0:
		adjacentPositions.append([row - 1, col])
	#check if there is a neighbor below us
	if row < len(matrix) - 1:
		adjacentPositions.append([row + 1, col])
	#check if there is a neighbor to the left
	if col > 0:
		adjacentPositions.append([row, col - 1])
	#check if there is a neighbor to the right
	if col < len(matrix[0]) - 1:
		adjacentPositions.append([row, col + 1])

	return adjacentPositions



def containsNegative(matrix):
	for row in matrix:
		for value in row:
			if value < 0:
				return True
	return False

