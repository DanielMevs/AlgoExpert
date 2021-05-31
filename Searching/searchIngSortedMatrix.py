#O(n + m) because that is the worst case that we start from the 
#right up corner and end up in the left bottom corner.
#O(1) space because we traverse in place

def searchInSortedMatrix(matrix, target):
	row = 0
	col = len(matrix[0]) - 1

	while row < len(matrix) and col >= 0:
		if matrix[row][col] > target:
			col -= 1
		elif matrix[row][col] < target:
			row += 1 
		else:
			return [row, col]
			
	return [-1, -1]
