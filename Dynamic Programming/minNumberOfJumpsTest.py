def minNumberOfJumps(array):
    jumps = [float("inf") for x in array]
    jumps[0] = 0
	
    for i in range(1, len(array)):
    	for j in range(0, i):
			print(f"jumps: {jumps}")
			print("j = ", j)
			print("array[j] = ", array[j])
			print("i: ", i)
			print("array[j] + j", array[j] + j)
    		if array[j] + j >= i:
				print("-----------")
				print("jumps[j]: ", jump[j])
				print("jumps[j] + j", jumps[j] + j)
				minVal = min(jumps[j] + 1, jumps[i])
				print("Min of jump[j] + 1 and jumps[i]: ", minVal)
				print("old jumps: ", jumps)
    			jumps[i] = minVal
				print("new jumps: ", jumps)			
			   	print("------------")
			print("\n")

    return jumps[-1]