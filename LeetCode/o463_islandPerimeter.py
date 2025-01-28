class Solution(object):
    def islandPerimeter(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        ans = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    ans += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        ans -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        ans -= 2

        return ans
    
    def islandPerimeter2(self, grid): #beats %19
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(grid, r, c):
            # print(f"r: {r}, c: {c}")
            line = 0
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0
            grid[r][c] = -1
                      
            for dr, dc in directions:            
                line += dfs(grid, r+dr, c+dc)
            return line
        
        for sr in range(ROWS):
            for sc in range(COLS):
                if grid[sr][sc] == 1:
                    return dfs(grid, sr, sc)
        return 0

sol = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print("")
print(f"grid: {grid}")
print(f"16 => {sol.islandPerimeter(grid)}") 
grid = [[0,1]]
print("")
print(f"grid: {grid}")
print(f"4 => {sol.islandPerimeter(grid)}") 
                
# 463. Island Perimeter
# Easy

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4