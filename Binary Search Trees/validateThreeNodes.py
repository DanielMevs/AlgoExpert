# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#O(h) time | O(h) space
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDescendant(nodeTwo, nodeOne):
    	return isDescendant(nodeThree, nodeTwo)

    if isDescendant(nodeTwo, nodeThree):
    	return isDescendant(nodeOne, nodeTwo)

    return False

def isDescendant(node, target):
	if node is None:
		return False

	if node is target:
		return True

	return isDescendant(node.left, target) if target.value < node.value else isDescendant(node.right, target)

#Solution 2, better space
#O(h) time : h = height of tree
#O(1) space : iterative implementation
def isDescendant(node, target):
	while  node is not None and node is not target:
		node = node.left if node.value > target.value else node.right

	return node is target

#solution 3, better time and space
#O(d) average time : d = distance between nodeOne and nodeThree
#O(h) worst case
#O(1) space
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
	searchOne = nodeOne
	searchTwo = nodeThree

	while True:
		#BREAK CONDITIONS#

		#we found node three from node one
		foundThreeFromOne = searchOne is nodeThree

		#we found node one from node three
		foundOneFromThree = searchTwo is nodeOne

		#we found node two from either of the two nodes
		foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo

		#both nodes that we are on are currently equal to none
		finishedSearching = searchOne is None and searchTwo is None

		if foundThreeFromOne or foundOneFromThree or foundNodeTwo or finishedSearching:
			break

		if searchOne is not None:
			searchOne = searchOne.left if searchOne.value > nodeTwo.value else searchOne.right

		if searchTwo is not None:
			searchTwo = searchTwo.left if searchTwo.value > nodeTwo.value else searchTwo.right

	foundNodeFromOther = searchOne is nodeThree or searchTwo is nodeOne
	foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo

	if not foundNodeTwo or foundNodeFromOther:
		return False

	#if searchOne is equal to nodeTwo, nodeOne was our ancestor => check if nodeThree is descendant
	#else we found nodeTwo from nodeThree => check if nodeOne is a descendant of nodeTwo
	return searchForTarget(nodeTwo, nodeThree if searchOne is nodeTwo else nodeOne)


def searchForTarget(node, target):
	while  node is not None and node is not target:
		node = node.left if target.value < node.value else node.right

	return node is target