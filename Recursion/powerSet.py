def powerset(array):
    subSets = [[]]
	for ele in array:
		for i in range(len(subSets)):
			currentSubset = subSets[i]
			subSets.append(currentSubset + [ele])
	return subSets
