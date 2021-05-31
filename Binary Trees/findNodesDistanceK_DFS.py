class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#O(n) time
#O(n) space
def findNodesDistanceK(tree, target, k):
	nodesDistanceK = []
	findDistanceFromNodeToTarget(tree, target, k, nodesDistanceK)
	return nodesDistanceK

def findDistanceFromNodeToTarget(node, target, k, nodesDistanceK):
	if node is None:
		#indicator that we did not find the target node
		return -1

	if node.value == target:
		addSubtreeNodesAtDistanceK(node, 0, k, nodesDistanceK)
		return 1

	#these variables tell you how far away the currrent node is from the target node in the left or right subtree
	#if node.left or node.right gives you 1, then that was the target node and it's 1 away from it
	leftDistance = findDistanceFromNodeToTarget(node.left, target, k, nodesDistanceK)
	rightDistance = findDistanceFromNodeToTarget(node.right, target, k, nodesDistanceK)

	#current node is k distance away from the target node
	if leftDistance == k or rightDistance == k:
		nodesDistanceK.append(node.value)


	if leftDistance != -1:
		addSubtreeNodesAtDistanceK(node.right, leftDistance + 1, k, nodesDistanceK)
		return leftDistance + 1

	if rightDistance != -1:
		addSubtreeNodesAtDistanceK(node.left, rightDistance + 1, k, nodesDistanceK)
		return rightDistance + 1

	return -1


def addSubtreeNodesAtDistanceK(node, distance, k, nodesDistanceK):
	if node is None:
		return

	if distance == k:
		nodesDistanceK.append(node.value)
	else:
		addSubtreeNodesAtDistanceK(node.left, distance + 1, k, nodesDistanceK)
		addSubtreeNodesAtDistanceK(node.right, distance + 1, k, nodesDistanceK)



