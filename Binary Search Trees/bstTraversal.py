def inOrderTraverse(tree, array):
	if(tree.left != None):
		inOrderTraverse(tree.left, array)
	array.append(tree.value)
	if(tree.right != None):
		inOrderTraverse(tree.right, array)
		
	return array
    # Write your code here.
    


def preOrderTraverse(tree, array):
	array.append(tree.value)
    if(tree.left != None):
		preOrderTraverse(tree.left, array)

	if(tree.right != None):
		preOrderTraverse(tree.right, array)

	return array


def postOrderTraverse(tree, array):
    
    if(tree.left != None):
		postOrderTraverse(tree.left, array)

	if(tree.right != None):
		postOrderTraverse(tree.right, array)
	array.append(tree.value)
	return array
