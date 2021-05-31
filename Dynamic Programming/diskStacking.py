#Given a non-empty array of arrays where each subarray holds three integers and represents a disk.
#These integers denote each disk's width, depth, and height, respectively.
#A disk must have a strictly smaller width, depth, and height than any other disk below it.
#Write a function that returns an array of the disks in the final stack, starting with the top disk 
#and ending with the bottom disk.

#O(N^2) time: N = len(input_array)
#O(N) space : N = len(input_array)
def diskStacking(disks):
	#disk[2] indicates that we want to sort the array by the 3rd element in our array;
	#in this case the height.
    disks.sort(key = lambda disk: disk[2])
    # for disk in disks:
    # 	heights.append(disk[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]
    maxHeightIdx = 0
    
    for i in range(1, len(disks)):
    	currentDisk = disks[i]
    	for j in range(0, i):
    		otherDisk = disks[j]
    		if areValidDimensions(otherDisk, currentDisk):
    			if heights[i] <= currentDisk[2] + heights[j]:
    				heights[i] = currentDisk[2] + heights[j]
    				sequences[i] = j
    	if heights[i] >= heights[maxHeightIdx]:
    		maxHeightIdx = i

    return buildSequence(disks, sequences, maxHeightIdx)


#o = otherDisk ; c = currentDisk
def areValidDimensions(o, c):
	#one-liner returns a boolean
	return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

def buildSequence(array, sequences, currentIdx):
	sequence = []
	while currentIdx is not None:
		sequence.append(array[currentIdx])
		currentIdx = sequences[currentIdx]
	return list(reversed(sequence))