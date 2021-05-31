# O(n) time; O(1) space : n = length of array
def threeNumberSort(array, order):
    # buckets to keep track of count of each of the values in order array
    valueCounts = [0, 0, 0]
    for element in array:
        orderIdx = order.index(element)
        valueCounts[orderIdx] += 1
    for i in range(3):
        value = order[i]
        count = valueCounts[i]

        numElementsBefore = sum(valueCounts[:i])
        for n in range(count):
            currentIdx = numElementsBefore + n
            array[currentIdx] = value
    return array

# O(n) time; O(1) space : n = length of array


def threeNumberSort(array, order):
    firstValue = order[0]
    thirdValue = order[2]

    firstIdx = 0
    for idx in range(len(array)):
        if array[idx] == firstValue:
            array[firstIdx], array[idx] = array[idx], array[firstIdx]
            firstIdx += 1
    thirdIdx = len(array) - 1
    for idx in range(len(array) - 1, -1, -1):
        if array[idx] == thirdValue:
            array[thirdIdx], array[idx] = array[idx], array[thirdIdx]
            thirdIdx -= 1

    return array

# O(n) time; O(1) space : n = length of array


def threeNumberSort(array, order):
    firstValue = order[0]
    secondValue = order[1]

    # Keep track of the indices where the values are stored
    firstIdx, secondIdx, thirdIdx = 0, 0, len(array) - 1

    while secondIdx <= thirdIdx:
        value = array[secondIdx]

        if value == firstValue:
            array[secondIdx], array[firstIdx] = array[firstIdx], array[secondIdx]
            firstIdx += 1
            secondIdx += 1
        elif value == secondValue:
            secondIdx += 1
        else:
            array[secondIdx], array[thirdIdx] = array[thirdIdx], array[secondIdx]
            thirdIdx -= 1
	return array
