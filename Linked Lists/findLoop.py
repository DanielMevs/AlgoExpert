#write a function that takes in the head of a Singly Linked list
#that contains a loop (in other words, the list's tail node points
# to some node in the list instead of None/ Null)
#The function should return the node from which the loop
#originates in constant time


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#O(n) time | O(1) space
def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:
    	first = first.next
    	second = second.next.next
    first = head
    while first != second:
    	first = first.next
    	second = second.next
    return first
