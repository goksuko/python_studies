from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS): # first find the treasures
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        print(q)
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
        
        print(grid)
        
sol = Solution()
Input = [[2147483647,-1,0,2147483647],
  	[2147483647,2147483647,2147483647,-1],
  	[2147483647,-1,2147483647,-1],
 	[0,-1,2147483647,2147483647]
]        
print("")
# print(f"nums: {Input}")
print(Input)
print(f"[[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]] => \n{sol.islandsAndTreasure(Input)}")                       
                    
        


# Islands and Treasure
# You are given a m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Example 1:

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
# Example 2:

# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]

# Output: [
#   [0,-1],
#   [1,2]
# ]
# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is one of {-1, 0, 2147483647}


# Recommended Time & Space Complexity
# You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the given grid.


# Hint 1
# A brute force solution would be to iterate on each land cell and run a BFS from that cells to find the nearest treasure chest. This would be an O((m * n)^2) solution. Can you think of a better way? Sometimes it is not optimal to go from source to destination.


# Hint 2
# We can see that instead of going from every cell to find the nearest treasure chest, we can do it in reverse. We can just do a BFS from all the treasure chests in grid and just explore all possible paths from those chests. Why? Because in this approach, the treasure chests self mark the cells level by level and the level number will be the distance from that cell to a treasure chest. We don't revisit a cell. This approach is called Multi-Source BFS. How would you implement it?


# Hint 3
# We insert all the cells (row, col) that represent the treasure chests into the queue. Then, we process the cells level by level, handling all the current cells in the queue at once. For each cell, we mark it as visited and store the current level value as the distance at that cell. We then try to add the neighboring cells (adjacent cells) to the queue, but only if they have not been visited and are land cells.

