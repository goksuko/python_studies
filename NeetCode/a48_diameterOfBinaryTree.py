from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right) # updates res to be the max of its current value and the sum of the left and the right
            # it actually calculated the diameter passing through the current node
            return 1 + max(left, right) # returns the height of the current node

        dfs(root)
        return res


# Diameter of Binary Tree
# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

# The length of a path between two nodes in a binary tree is the number of edges between the nodes.

# Given the root of a binary tree root, return the diameter of the tree.

# Example 1:



# Input: root = [1,null,2,3,4,5]

# Output: 3
# Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

# Example 2:

# Input: root = [1,2,3]

# Output: 2
# Constraints:

# 1 <= number of nodes in the tree <= 100
# -100 <= Node.val <= 100


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the tree.


# Hint 1
# The diameter of a binary tree is the maximum among the sums of the left height and right height of the nodes in the tree. Why?


# Hint 2
# Because the diameter of a binary tree is defined as the longest path between any two nodes in the tree. The path may or may not pass through the root. For any given node, the longest path that passes through it is the sum of the height of its left subtree and the height of its right subtree.


# Hint 3
# A brute force solution would be to go through every node in the tree and compute its left height and right height, returning the maximum diameter found. This would be an O(n^2) solution. Can you think of a better way? Maybe we can compute the diameter as we calculate the height of the tree? Think about what information you need from each subtree during a single traversal.


# Hint 4
# We can use the Depth First Search (DFS) algorithm to calculate the height of the tree. At each node, the subtrees return their respective heights (leftHeight and rightHeight). Then we calculate the diameter at that node as d = leftHeight + rightHeight. We use a global variable to update the maximum diameter as needed during the traversal.