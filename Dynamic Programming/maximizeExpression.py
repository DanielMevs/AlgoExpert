#Write a function that takes in an array of integers and returns
#the largest possible value for the expression 
#array[a] - array[b] + array[c] - array[d], where a, b, c, and d
#are indices of the array and a < b < c < d.


def maximizeExpression(array):
    if len(array) < 4: 
    	return 0

    maximumValueFound = float('-inf')

    for a in range(len(array)):
    	aValue = array[a]
    	for b in range(a + 1, len(array)):
    		bValue = array[b]
    		for c in range(b + 1, len(array)):
    			cValue = array[c]
    			for d in range(c + 1, len(array)):
    				dValue = array[d]
    				expressionValue = evaluateExpression(aValue, bValue, cValue, dValue)
    				maximumValueFound = max(expressionValue, maximumValueFound)
    return maximumValueFound

def evaluateExpression(a, b, c, d):
	return a - b + c - d

