def mergeOverlappingIntervals(intervals):
    # Sort intervals by starting value
	sortedIntervals = sorted(intervals, key=lambda x: x[0])
	
	mergedIntervals = []
	currentInterval = sortedIntervals[0]
	mergedIntervals.append(currentInterval)
	
	for nextInterval in sortedIntervals:
		#we extract the ending value as we are not interested
		#in the the starting value
		_, currentIntervalEnd = currentInterval
		nextIntervalStart, nextIntervalEnd = nextInterval
		
		if currentIntervalEnd >= nextIntervalStart:
			currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
		else:
			currentInterval = nextInterval
			mergedIntervals.append(currentInterval)
			
	return mergedIntervals