#write a function that takes in the head of a Singly Linked List
#and an integer k, shifts the list in place by k positions, and returns
#its new head.

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#O(n) time | O(1) space
def shiftLinkedList(head, k):
    listLength = 1
    listTail = head
    while listTail.next is not None:
    	listTail = listTail.next
    	listLength += 1

    offset = abs(k) % listLength
    if offset == 0:
    	return head

    newTailPosition = listLength - offset if k > 0 else offset
    newTail = head
    for i in range(1, newTailPosition):
    	newTail = newTail.next

    newHead = newTail.next
    newTail.next = None
    listTail.next = head
    return newHead