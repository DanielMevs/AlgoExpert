# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

#O(n) time, O(n) space
def findSuccessor1(tree, node):
	inOrderTraversalOrder = getInOrderTraversalOrder(tree)
	
	for idx, currentNode in enumerate(inOrderTraversalOrder):
		if currentNode != node:
			continue
		if idx == len(inOrderTraversalOrder) - 1:
			return None
		return inOrderTraversalOrder[idx + 1]
    

def getInOrderTraversalOrder(node, order=[]):
	if node is None:
		return order
	
	getInOrderTraversalOrder(node.left, order)
	order.append(node)
	getInOrderTraversalOrder(node.right, order)
	
	return order


#O(h) time | O(1) space
def findSuccessor2(tree, node):
	if node.right is not None:
		return getLeftmostChild(node.right)
	
	return getRightmostParent(node)
	

def getLeftmostChild(node):
	currentNode = node.right
	while currentNode.left is not None:
		currentNode = currentNode.left
		
	return currentNode

def getRightmostParent(node):
	currentNode = node
	while currentNode.parent is not None and currentNode.parent.right == currentNode:
		currentNode = currentNode.parent
	
	return currentNode.parent
	