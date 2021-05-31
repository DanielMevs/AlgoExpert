#O(n^2) time] | O(1) space
def longestPalindromicSubstring(string):
    currentLongest = [0,1]
    #we start at 1 because we assume the first character is a palindrome.
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i-1, i+1) #represents the left and right index that we're trying to expand
        even = getLongestPalindromeFrom(string, i-1, i) #our center is between i-1 and i
        #we take the greatest of odd and even.
        #The metric we use is which palindrome has a greater difference
        #between its second index(the end of the string) and the first index(the start of the string)
        longest = max(odd, even, key= lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
    return string[currentLongest[0]: currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]
