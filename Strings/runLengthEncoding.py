def runLengthEncoding(string):
    # Write your code here.
	newStringChars = []
	currentLen = 1
	
	for i in range(1, len(string)):
		if string[i-1] != string[i] or currentLen == 9:
			newStringChars.append(str(currentLen))
			newStringChars.append(string[i-1])
			currentLen = 0
			
		currentLen += 1
		
	newStringChars.append(str(currentLen))
	newStringChars.append(string[len(string) -1 ])
	
	return "".join(newStringChars)
		
    pass
