def cycleInGraph(edges):
    numberOfNodes = len(edges) #number of vertices in our graph
    visited = [False for _ in range(numberOfNodes)]
    currentlyInStack = [False for _ in range(numberOfNodes)]

    for node in range(numberOfNodes):
    	if visited[node]:
    		continue

    	#run dfs
    	containsCycle = isNodeInCycle(edges, node, visited, currentlyInStack)
    	if containsCycle:
    		return True

    return False

def isNodeInCycle(edges, node, visited, currentlyInStack):
	visited[node] = True
	currentlyInStack[node] = True

	neighbors = edges[node]
	for neighbor in neighbors:
		if not visited[neighbor]:
			containsCycle = isNodeInCycle(edges, neighbor, visited, currentlyInStack)
			if containsCycle:
				return True
		elif currentlyInStack[neighbor]:
			return True

	#making sure that when we get to the end of this function
	#we define that this function call has ended
	#and that the current node is no longer in the recursive stack
	currentlyInStack[node] = False

