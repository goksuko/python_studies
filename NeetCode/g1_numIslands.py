from typing import List

class Solution:
    # 1. Depth First Search
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfc(r: int, c: int):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return
            
            grid[r][c] = 0
            for dr, dc in directions:
                dfc(r + dr,c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    islands += 1
                    dfc(r, c)
        
        return islands



# Number of Islands
# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

# Example 1:

# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1
# Example 2:

# Input: grid = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
# Output: 4
# Constraints:

# 1 <= grid.length, grid[i].length <= 100
# grid[i][j] is '0' or '1'.


# Recommended Time & Space Complexity
# You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the grid.


# Hint 1
# An island is a group of 1's in which every 1 is reachable from any other 1 in that group. Can you think of an algorithm that can find the number of groups by visiting a group only once? Maybe there is a recursive way of doing it.


# Hint 2
# We can use the Depth First Search (DFS) algorithm to traverse each group independently. We iterate through each cell of the grid. When we encounter a 1, we perform a DFS starting at that cell and recursively visit every other 1 that is reachable. During this process, we mark the visited 1's as 0 to ensure we don't revisit them, as they belong to the same group. The number of groups corresponds to the number of islands.