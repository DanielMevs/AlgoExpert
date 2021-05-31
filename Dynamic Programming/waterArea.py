#Given a array of non-negative integers, where each integer represents
#the height of a pillar of width 1. Imagine water being poured over all the pillars.
#Write a function that returns the surface area of the water trapped between the pillars 
#viewed from the front.

#O(n) time | O(n) space
def waterArea(heights):
    maxes = [0 for x in heights]
    leftMax = 0

    for i in range(len(heights)):
    	height = heights[i]
    	maxes[i] = leftMax
    	leftMax = max(leftMax, height)

    rightMax = 0
    for i in reversed(range(len(heights))):
    	height = heights[i]
    	minHeight = min(rightMax, maxes[i])
    	if height < minHeight:
    		maxes[i] = minHeight - height
    	else:
    		maxes[i] = 0

    	rightMax = max(rightMax, height)

    return sum(maxes)