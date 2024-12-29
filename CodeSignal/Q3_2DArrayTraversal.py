#https://codesignal.com/blog/interview-prep/example-codesignal-questions/

from typing import List

#codesignal
def solution(field, figure):
    height = len(field)
    width = len(field[0])
    figure_size = len(figure)
    
    for column in range(width - figure_size + 1): # to check the positons
        row = 1
        while row < height - figure_size + 1:
            can_fit = True
            for dx in range(figure_size):
                for dy in range(figure_size):
                    if field[row + dx][column + dy] == 1 and figure[dx][dy] == 1:
                        can_fit = False #when we start from the row, coloumn, the object can not fit there
            if not can_fit: #if it cannot fit, then break the while loop and decrement row by 1 and check later for that position 
                break
            row += 1
        row -= 1
    
        for dx in range(figure_size):
            row_filled = True
            for column_index in range(width):
                if not (field[row + dx][column_index] == 1 or
                        (column <= column_index < column + figure_size and
                    figure[dx][column_index - column] == 1)):
                    row_filled = False
            if row_filled:
                return column
    return -1

class Solution:
    def twoDArray(self, field: List[List], figure: List[List]) -> int:
        ans = -1
        height = len(field)
        width = len(field[0])
        figure_size = len(figure)      
        for i in range(width - figure_size + 1): # to check the positons
            for j in range(figure_size): # to check every coloumn in object
                ok = True                
                for k in range(figure_size): # to check every row in object
                    for l in range(height - figure_size + 1): # to check while it was dropping
                        print(f"field[{k}][{j + i}] + figure[{k}][{j}]: {field[k][j + i]} + {figure[k][j]}")
                        if field[k + l][j + i] + figure[k][j] > 1: # it will not fit in that position
                            break
                        elif field[k + l][j + i] + figure[k][j] != 1:
                            ok = False
            if ok:
                return i    
        return ans
    
    # this solves only last line
    def twoDArray2(self, field: List[List], figure: List[List]) -> int:
        ans = -1
      
        for i in range(len(field[0]) - len(figure[0]) + 1): # to check the positons
            j = 0
            while j < len(figure[0]): # to check every coloumn in object
                if field[-1][j] + figure[-1][j] != 1:
                    break
                j += 1
            if j == len(figure[0]):
                return i            
        return ans
        
        
        
        
sol = Solution()
field = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [1, 0, 0],
         [1, 1, 0]]
figure = [[0, 0, 1],
         [0, 1, 1],
         [0, 0, 1]]
print("")
print(f"field: {field}")
print(f"figure: {figure}")
print(f"0 => {sol.twoDArray(field, figure)}")     
field =  [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [1, 1, 0, 1, 0],
          [1, 0, 1, 0, 1]]
figure = [[1, 1, 1],
          [1, 0, 1],
          [1, 0, 1]]
print("")
print(f"field: {field}")
print(f"figure: {figure}")
print(f"2 => {sol.twoDArray(field, figure)}")         
field =  [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 1],
          [1, 1, 0, 1]]
figure = [[1, 1, 0],
          [1, 0, 0],
          [1, 0, 0]]
print("")
print(f"field: {field}")
print(f"figure: {figure}")
print(f"-1 => {sol.twoDArray(field, figure)}")    

# You are given a matrix of integers field of size height × width representing a game field, and also a matrix of integers figure of size 3 × 3 representing a figure. Both matrices contain only 0s and 1s, where 1 means that the cell is occupied, and 0 means that the cell is free.

# You choose a position at the top of the game field where you put the figure and then drop it down. The figure falls down until it either reaches the ground (bottom of the field) or lands on an occupied cell, which blocks it from falling further. After the figure has stopped falling, some of the rows in the field may become fully occupied.

# demonstration

# Your task is to find the dropping position such that at least one full row is formed. As a dropping position, you should return the column index of the cell in the game field which matches the top left corner of the figure’s 3 × 3 matrix. If there are multiple dropping positions satisfying the condition, feel free to return any of them. If there are no such dropping positions, return -1.

# Note: The figure must be dropped so that its entire 3 × 3 matrix fits inside the field, even if part of the matrix is empty. 

# Example

# For
# field = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0],
#          [1, 0, 0],
#          [1, 1, 0]]
# and
# figure = [[0, 0, 1],
#          [0, 1, 1],
#          [0, 0, 1]]

# the output should be solution(field, figure) = 0.

# Because the field is a 3 x 3 matrix, the figure can be dropped only from position 0. When the figure stops falling, two fully occupied rows are formed, so dropping position 0 satisfies the condition.

# example 1

# For
# field =  [[0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [1, 1, 0, 1, 0],
#           [1, 0, 1, 0, 1]]

# and
# figure = [[1, 1, 1],
#           [1, 0, 1],
#           [1, 0, 1]]

# the output should be solution(field, figure) = 2.

# The figure can be dropped from three positions: 0, 1, and 2. As you can see below, a fully occupied row will be formed only when dropping from position 2:

# example 2

# For
# field =  [[0, 0, 0, 0],
#           [0, 0, 0, 0],
#           [0, 0, 0, 0],
#           [1, 0, 0, 1],
#           [1, 1, 0, 1]]

# and
# figure = [[1, 1, 0],
#           [1, 0, 0],
#           [1, 0, 0]]

# the output should be solution(field, figure) = -1.

# The figure can be dropped from two positions, 0 and 1, and in both cases, a fully occupied row won’t be obtained:

# example 3

# Note that the figure could technically form a full row if it was dropped one position further to the right, but that is not a valid dropping position, because the 3 x 3 figure matrix wouldn’t be fully contained within the field.