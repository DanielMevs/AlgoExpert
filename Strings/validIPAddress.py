def validIPAddresses(string):
	validIPAddressesFound = []

	for i in range(1, min(len(string), 4)):
		currentIPAddressParts = ['', '', '', '']

		currentIPAddressParts[0] = string[:i]
		if not isValidPart(currentIPAddressParts[0]):
			continue
		#we do len(string)-i to avoid an index error
		for j in range(i + 1, i + min(len(string) - i, 4)):
			currentIPAddressParts[1] = string[i: j]
			if not isValidPart(currentIPAddressParts[1]):
				continue
			for k in range(j + 1, j + min(len(string) - j, 4)):
				currentIPAddressParts[2] = string[j:k]
				currentIPAddressParts[3] = string[k:]

				if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
					validIPAddressesFound.append('.'.join(currentIPAddressParts))
					
	return validIPAddressesFound

def isValidPart(string):
	stringAsInt = int(string) 
	if stringAsInt > 255:
		return False
	#trying to remove any trailing zeros eg 01, 001
	return len(string) == len(str(stringAsInt))