from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
                r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


sol = Solution()
heights = [[4,2,7,3,4],[7,4,6,4,7],[6,3,5,3,6]]
print("")
print(f"heights: {heights}")
print(f"[[0, 2], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0]] => \n{sol.pacificAtlantic(heights)}")   
heights = [[1],[1]]
print("")
print(f"heights: {heights}")
print(f"[[0, 0], [1, 0]] => \n{sol.pacificAtlantic(heights)}")   

# Pacific Atlantic Water Flow
# You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

# Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

# Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

# Example 1:



# Input: heights = [
#   [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]

# Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
# Example 2:

# Input: heights = [[1],[1]]

# Output: [[0,0],[1,0]]
# Constraints:

# 1 <= heights.length, heights[r].length <= 100
# 0 <= heights[r][c] <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the grid.


# Hint 1
# A brute force solution would be to traverse each cell in the grid and run a BFS from each cell to check if it can reach both oceans. This would result in an O((m * n)^2) solution. Can you think of a better way? Maybe you should consider a reverse way of traversing.


# Hint 2
# We can use the Depth First Search (DFS) algorithm starting from the border cells of the grid. However, we reverse the condition such that the next visiting cell should have a height greater than or equal to the current cell. For the top and left borders connected to the Pacific Ocean, we use a hash set called pacific and run a DFS from each of these cells, visiting nodes recursively. Similarly, for the bottom and right borders connected to the Atlantic Ocean, we use a hash set called atlantic and run a DFS. The required coordinates are the cells that exist in both the pacific and atlantic sets. How do you implement this?


# Hint 3
# We perform DFS from the border cells, using their respective hash sets. During the DFS, we recursively visit the neighbouring cells that are unvisited and have height greater than or equal to the current cell's height and add the current cell's coordinates to the corresponding hash set. Once the DFS completes, we traverse the grid and check if a cell exists in both the hash sets. If so, we add that cell to the result list.