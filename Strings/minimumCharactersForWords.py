#Write a function that takes in an array of words and returns
# the smallest array of characters needed to form all the words.

#O(n * l) time | O(c) space
def minimumCharactersForWords(words):
    maximumCharacterFrequencies = {}
    for word in words:
    	characterFrequencies = countCharacterFrequencies(word)
    	updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies)

    return makeArrayFromCharacterFrequencies(maximumCharacterFrequencies)

def countCharacterFrequencies(string):
	characterFrequencies = {}
	for character in string:
		if character not in characterFrequencies:
			characterFrequencies[character] = 0
		characterFrequencies[character] += 1
	return characterFrequencies

def updateMaximumFrequencies(frequencies, maximumFrequencies):
	for character in frequencies:
		frequency = frequencies[character]

		if character in maximumFrequencies:
			maximumFrequencies[character] = max(frequency, maximumFrequencies[character])
		else:
			maximumFrequencies[character] = frequency


def makeArrayFromCharacterFrequencies(characterFrequencies):
	characters = []

	for character in characterFrequencies:
		frequency = characterFrequencies[character]

		for _ in range(frequency):
			characters.append(character)

	return characters