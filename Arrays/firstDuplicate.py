def firstDuplicateValue(array):
	compare = []
	#compare = set()
	for i in range(0,len(array)):
		if array[i] not in compare:
			compare.append(array[i])
			#compare.add(array[i])
		else:
			return array[i]
    # Write your code here.
    return -1
