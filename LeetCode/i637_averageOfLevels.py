from collections import deque
from collections import defaultdict
from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution2:   
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        lvlcnt = defaultdict(int)
        lvlsum = defaultdict(int)

        def dfs(node=root, level=0):
            if not node: return
            lvlcnt[level] += 1
            lvlsum[level] += node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            
        dfs()
        return [round(lvlsum[i] / lvlcnt[i], 5) for i in range(len(lvlcnt))]

class Solution:
    def __init__(self):
        # Map with key as level of the tree,
        # map[level] = {sum of the level, number of elements in the level}
        self.mp = defaultdict(lambda: [0.0, 0.0])

    # Function to calculate the sum and count of nodes at each level
    def avg(self, root: TreeNode, l: int) -> None:
        # If the node is a leaf node, return
        if not root:
            return

        # Add the current value to the sum of this level
        self.mp[l][0] += root.val

        # Increase the number of elements in the current level
        self.mp[l][1] += 1

        # Traverse left subtree
        self.avg(root.left, l + 1)

        # Traverse right subtree
        self.avg(root.right, l + 1)

    # Function to compute the average of levels in a binary tree
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # Resultant list
        ans = []

        # Calculate sum and count of nodes at each level
        self.avg(root, 0)

        # Iterate over the map to compute the average at each level
        for level, (sum_level, count) in sorted(self.mp.items()):
            ans.append(sum_level / count)

        return ans
        
        
# Create the example tree [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Create an instance of Solution2 and call averageOfLevels
solution = Solution2()
output = solution.averageOfLevels(root)
print(output)  # Expected output: [3.00000, 14.50000, 11.00000]

# 637. Average of Levels in Binary Tree
# Easy

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual numswer will be accepted.
 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
# Example 2:


# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1