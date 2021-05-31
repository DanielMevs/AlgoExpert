#O(N) time : N = # of nodes in the tree (we traverse N nodes)
#O(log(N)) space : we are dealing with a binary tree (there will be an average of log(n) nodes accumulated on the call stack)
def maxPathSum(tree):
	#we do not care about the first value
	_, maxSum = findMaxSum(tree)
	return maxSum

def findMaxSum(tree):
	if tree is None:
		return (0, float("-inf"))

	#THE BLOCK BELOW CONSISTS OF CONSTANT TIME OPERATIONS
	leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
	rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
	maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

	value = tree.value

	#maxSumAsBranch: the max sum as a branch that we can comfortably use
	#to compute values higher up in our tree
	maxSumAsBranch = max(maxChildSumAsBranch + value, value)

	#leftMaxSumAsBranch + value + rightMaxSumAsBranch indicates a triangle
	maxSumAsRootNode = max(maxSumAsBranch, leftMaxSumAsBranch + value + rightMaxSumAsBranch)

	#maxPathSum: running max path sum takes into account the left running max path sum, 
	#the right running max path sum, and our max path sum as a potential triangle
	maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

	return (maxSumAsBranch, maxPathSum)