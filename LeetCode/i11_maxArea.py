class Solution(object): 
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        width = len(height)
        water = 0
        i = 0
        j = width - 1
        while (i <= j):
            temp = min(height[i], height[j]) * (j - i)
            water = max(temp, water)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return water
            
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        cr = 0

        while i != j:
            length = max(i+1,j+1) - min(i+1,j+1)

            if height[i] >= height[j]:
                volume = height[j] * length
                j-=1
            else:
                volume = height[i] * length
                i+=1
            if volume > cr:
                cr = volume
        
        return(cr)        
        
sol = Solution()
print("49: ", sol.maxArea([1,8,6,2,5,4,8,3,7]))
print("1: ", sol.maxArea([1,1]))



# 11. Container With Most Water
# Medium

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104