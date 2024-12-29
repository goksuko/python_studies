from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        
        def dfc(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return (1 + dfc(r + 1, c) + 
                        dfc(r - 1, c) + 
                        dfc(r, c + 1) + 
                        dfc(r, c - 1))            
    
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfc(r,c))
        
        return maxArea

sol = Solution()
nums = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
print("")
print(f"nums: {nums}")
print(f"6 => {sol.maxAreaOfIsland(nums)}")     

# Max Area of Island
# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

# The area of an island is defined as the number of cells within the island.

# Return the maximum area of an island in grid. If no island exists, return 0.

# Example 1:



# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]

# Output: 6
# Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

# Constraints:

# 1 <= grid.length, grid[i].length <= 50


# Recommended Time & Space Complexity
# You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the grid.


# Hint 1
# An island is a group of 1's in which every 1 is reachable from any other 1 in that group. Can you think of an algorithm that can find the number of groups by visiting a group only once? Maybe there is a recursive way of doing it.


# Hint 2
# We can use the Depth First Search (DFS) algorithm to traverse each group by starting at a cell with 1 and recursively visiting all the cells that are reachable from that cell and are also 1. Can you think about how to find the area of that island? How would you implement this?


# Hint 3
# We traverse the grid, and when we encounter a 1, we initialize a variable area. We then start a DFS from that cell to visit all connected 1's recursively, marking them as 0 to indicate they are visited. At each recursion step, we increment area. After completing the DFS, we update maxArea, which tracks the maximum area of an island in the grid, if maxArea < area. Finally, after traversing the grid, we return maxArea.