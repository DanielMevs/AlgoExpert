# O(n) time | O(1) space
def kadanesAlgorithm(array):
    maxSoFar = array[0]
    maxSum = array[0]

    for num in array[1:]:
        maxSoFar = max(num, maxSoFar + num)
        if maxSoFar >= maxSum:
            maxSum = maxSoFar
    return maxSum


print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
