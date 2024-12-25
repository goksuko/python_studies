from typing import List

class Solution:
    # brute force
    def largestRectangleArea2(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        for i in range(n):
            height = heights[i]

            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1
            rightMost -= 1
            
            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1
            leftMost += 1
            
            maxArea = max(maxArea, height * (rightMost - leftMost + 1))
        return maxArea

# Time complexity: O(n^2)
# Space complexity: O(1)        

    # stack (optimal)
    def largestRectangleArea(self, heights: List[int]) -> int:       
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            print(f"i: {i}, h: {h}, start: {start}")
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
                print(f"in while start became {start}")
            stack.append((start, h))
            print(f"stack is appended by ({start}, {h})")

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
        
# Time complexity: O(n)
# Space complexity: O(n)


        
sol = Solution()
heights = [7,1,7,2,2,4]
print(f"\nheights: {heights}")
print(f"8 => {sol.largestRectangleArea(heights)}")
heights = [1,3,7]
print(f"\nheights: {heights}")
print(f"7 => {sol.largestRectangleArea(heights)}")


        


# Largest Rectangle In Histogram
# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

# Return the area of the largest rectangle that can be formed among the bars.

# Note: This chart is known as a histogram.

# Example 1:

# Input: heights = [7,1,7,2,2,4]

# Output: 8
# Example 2:

# Input: heights = [1,3,7]

# Output: 7
# Constraints:

# 1 <= heights.length <= 1000.
# 0 <= heights[i] <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A rectangle has a height and a width. Can you visualize how rectangles are formed in the given input? Considering one bar at a time might help. We can try to form rectangles by going through every bar and current bar's height will be the height of the rectangle. How can you determine the width of the rectangle for the current bar being the height of the rectangle? Extending the current bar to the left and right might help determine the rectangle's width.


# Hint 2
# For a bar with height h, try extending it to the left and right. We can see that we can't extend further when we encounter a bar with a smaller height than h. The width will be the number of bars within this extended range. A brute force solution would be to go through every bar and find the area of the rectangle it can form by extending towards the left and right. This would be an O(n^2) solution. Can you think of a better way? Maybe precomputing the left and right boundaries might be helpful.


# Hint 3
# The left and right boundaries are the positions up to which we can extend the bar at index i. The area of the rectangle will be height[i] * (right - left + 1), which is the general formula for height * width. These boundaries are determined by the first smaller bars encountered to the left and right of the current bar. How can we find the left and right boundaries now? Maybe a data structure is helpful.


# Hint 4
# We can use a stack with a monotonically strictly increasing nature, but instead of storing values, we store indices in the stack and perform operations based on the values at those indices. The top of the stack will represent the smaller bar that we encounter while extending the current bar. To find the left and right boundaries, we perform this algorithm from left to right and vice versa, storing the boundaries. Then, we iterate through the array to find the area for each bar and return the maximum area we get.