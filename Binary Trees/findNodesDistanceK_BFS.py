class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#O(n) time ; Breadth first search runs in O(v+e) time ;
# v= # of vertices, e = # of edges ; v + e < 2n => O(2n) => O(n)
#O(n) space ; seen set and parents data structure hold at most
#n element : n = # of nodes in tree
def findNodesDistanceK(tree, target, k):

    nodesToParents = {}
    populateNodesToParents(tree, nodesToParents)
    targetNode = getNodeFromValue(target, tree, nodesToParents)

    return breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k)

def breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k):
	#this will have a poor time complexity, as popping from the front of the list takes O(n) time 
	#to avoid this you can use a deque or a double-ended queue (available in the collections lib)
	queue = [(targetNode, 0)]
	seen = {targetNode.value}
	while len(queue) > 0:
		currentNode, disanceFromTarget = queue.pop(0) #not the optimal data structure for popping 

		if disanceFromTarget == k:
			nodesDistanceK = [node.value for node, _ in queue]
			nodesDistanceK.append(currentNode.value)
			return nodesDistanceK

		connectedNodes = [currentNode.left, currentNode.right, nodesToParents[currentNode.value]]

		for node in connectedNodes:

			if node is None:
				continue

			if node.value in seen:
				continue

			seen.add(node.value)
			queue.append((node, disanceFromTarget + 1))

	return []


def getNodeFromValue(value, tree, nodesToParents):

	if tree.value == value:
		return tree

	nodeParent = nodesToParents[value]

	if nodeParent.left and nodeParent.left.value == value:
		return nodeParent.left

	return nodeParent.right

def populateNodesToParents(node, nodesToParents, parent=None):
	if node:
		nodesToParents[node.value] = parent
		populateNodesToParents(node.left, nodesToParents, node)
		populateNodesToParents(node.right, nodesToParents, node)
