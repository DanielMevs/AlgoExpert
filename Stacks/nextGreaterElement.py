#Write a function that takes in an array of integers and 
#returns a new array containing, at each index, the next element 
#in the input array that's greater than the element at the index in
#the input array.
#Additionally, your function should treat the input array as a circular array.
#A circular array wraps around itself as if it were connected end-to-end.
#So the next index after the last index in a circular array is the first index.

#SampleInput:
#array = [2, 5, -3, -4, 6, 7, 2]
#Sample Output:
#[5, 6, 6, 6, 7, -1, 5]


#O(n) time | O(n) space
def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []

    for idx in range(2 * len(array)):
    	circularIdx = idx % len(array)

    	while len(stack) > 0 and array[stack[len(stack) - 1]] < array[circularIdx]:
    		top = stack.pop()
    		result[top] = array[circularIdx]

    	stack.append(circularIdx)

    return result



# BRUTE FORCE APPROACH
# Just look at every single element and simply loop through the result
# of the array and look for the first element we see that is greater
# than this element.

# i=0
# input --> [2, 5, -3, -4, 6, 7, 2]
# output--> [5, x,  x,  x, x, x, x]

# i=1
# input --> [2, 5, -3, -4, 6, 7, 2]
# output--> [5, x,  x,  x, x, x, x]

# i=2
# input --> [2, 5, -3, -4, 6, 7, 2]
# output--> [5, x,  x,  x, x, x, x]

# i=3
# input --> [2, 5, -3, -4, 6, 7, 2]
# output--> [5, x,  x,  x, x, x, x]

# i=4
# input --> [2, 5, -3, -4, 6, 7, 2]
# output--> [5, x,  x,  x, x, x, x]

# i=5
# input --> [2, 5, -3, -4, 6, 7, 2]
# output--> [5, x,  x,  x, x, x, x]

# i=6
# input --> [2, 5, -3, -4, 6, 7, 2]
# output--> [5, x,  x,  x, x, x, x]

# Complexity Analysis
# Time: O(n^2) --> for every element we have to potentially loop through
# every other element in the array to figure out the next greater element
# e.g. [1, 1, 1, 1, 1]
# Space: uses no extra space, other than the output array

# OPTIMAL SOLUTION
# O(N) time, O(N) space : N=len(input_array). Whenever you have a problem
# where you're looking for the maximum or the minimum, or the next element 
# that's greater than some element (or a lot of typical array problems really),
# you're able to actually solve these in linear time, using linear space.
# We will use some external space (a stack)
# Stack --> LIFO, FILO -> like a stack of plates
# We can use an array to implement a stack in our program
# Removing and adding elements to the stack is a constant-time operation (O(1))
# We're going to loop through the array, and at each step of our iteration,
# we're going to compare the value of the current element that we're on 
# to the value of the element on the top of the stack.

# We need to loop through this array twice because an element's next greatest
# element might be located later on in the array.
# We will use the modulus operator to help avoid index out of bound errors
# and effectively wrap around the array (e.g. j % len(array))

# i = 0
#   0          1   2   3   4   5   6
# [-1 X -> 5, -1, -1, -1, -1, -1, -1] --> result
#   stack
# | j=0 X| --> 0 -> result[0] = input[j] 
# | j=1  |	
#  0  1   2   3  4  5  6						
# [2, 5, -3, -4, 6, 7, 2] --> input
#  ^  ^
#  i! j /

#  _____________________________________________

#  i = 1
#  0   1          2          3          4   5   6
# [5, -1 X -> 6, -1 X -> 6, -1 X -> 6, -1, -1, -1] --> result
#   stack
# | j=4  | 
# | j=3 X|--> 3 -> result[3] = input[j] 
# | j=2 X|--> 2 -> result[2] = input[j]
# | j=1 X|--> 1 -> result[1] = input[j]

#  0  1   2   3  4  5  6						
# [2, 5, -3, -4, 6, 7, 2] --> input
#     ^   ^   ^  ^  
#     i!  j!  j! j /

# Now there's no more elements on the top of the stack.
# Now we add 4 to the top of the stack

#  _____________________________________________

#  i = 4
#  0  1  2  3   4          5   6
# [5, 6, 6, 6, -1 X -> 7, -1, -1] --> result
#   stack
# | j=5  |
# | j=4 X|--> 4 -> result[4] = input[j]

#  0  1   2   3  4  5  6						
# [2, 5, -3, -4, 6, 7, 2] --> input
#                ^  ^
#                i! j /

# There's no more elements on the top of the stack.
# Now we add 5 to the top of the stack.

# _____________________________________________

# i = 5
#  0         1  2  3   4          5   6
# [5 X -> 5, 6, 6, 6, -1 X -> 7, -1, -1 X -> 5] --> result
#   stack
# | j = 0 X|--> 0 -> result[0] = input[j] #repeatative work
# | j = 6 X|--> 6 -> result[6] = input[j] 
# | j = 5  |

#  0  1   2   3  4  5  6						
# [2, 5, -3, -4, 6, 7, 2] --> input
#  ^  ^             ^  ^
#  j! j  /          i! j!

#  We look at index 5 and see that input[5] is not less than
#  input[j] so we keep it on the stack and add 1 to the top
#  of the stack

#  _____________________________________________

#  i = 1
#  0  1         2         3          4   5   6
# [5, 6 X -> 6, 6 X -> 6, 6 X -> 6,  7, -1,  5] --> result
# stack
# | j = 3 X|--> 3 -> result[3] = input[j] #repeatative work
# | j = 2 X|--> 2 -> result[2] = input[j] #repeatative work
# | j = 1 X|--> 1 -> result[1] = input[j] #repeatative work
# | j = 5  |

#  0  1   2   3  4  5  6						
# [2, 5, -3, -4, 6, 7, 2] --> input
#     ^   ^   ^  ^
#     i!  j!  j! j /

# etc... return results

