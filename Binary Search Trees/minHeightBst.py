class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)




#space = O(N) as you are storing N values into nodes to insert to the tree.
#time = O(n(logn)) inserting a node in a binary tree takes logn time and we 
#are doing it for n nodes
#however there is an implemention st the insert can be in constant time
#making it O(N)
import math
def minHeightBst1(array, bst=None):
    middleIndex = math.floor(len(array) / 2)
	if bst == None:
		bst = BST(array[middleIndex])
	else:
		BST.insert(array[middleIndex])
		if(middleIndex != 0):
			minHeightBst(array[0:middleIndex])
			minHeightBst(arrray[middleIndex+1:len(array)])
			
		else:
			return bst


def minHeightBst2(array):
    return constructMinHeightBst(array, None, 0, len(array)-1)


def constructMinHeightBst2(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
        
    constructMinHeightBst(array, bst, startIdx, midIdx - 1)
    constructMinHeightBst(array, bst, midIdx + 1, endIdx)
    
    return bst

#O(n) time O(n) space
def constructMinHeightBst3(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
        
    bst.left = constructMinHeightBst(array, startIdx, midIdx - 1)
    bst.right = constructMinHeightBst(array, midIdx + 1, endIdx)
    
    return bst
                


