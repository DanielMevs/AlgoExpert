#Write a function that takes in the head of a Singly Linked
#List, reverses the list in place (i.e. doesn't create a brand new
#list), and returns its new head.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#O(n) time | O(1) space
def reverseLinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
    	nextNode = currentNode.next
    	currentNode.next = previousNode
    	previousNode = currentNode
    	currentNode = nextNode
    return previousNode
