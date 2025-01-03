from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

        


# Balanced Binary Tree
# Given a binary tree, return true if it is height-balanced and false otherwise.

# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:



# Input: root = [1,2,3,null,null,4]

# Output: true
# Example 2:



# Input: root = [1,2,3,null,null,4,null,5]

# Output: false
# Example 3:

# Input: root = []

# Output: true
# Constraints:

# The number of nodes in the tree is in the range [0, 1000].
# -1000 <= Node.val <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the tree.


# Hint 1
# A brute force solution would involve traversing every node and checking whether the tree rooted at each node is balanced by computing the heights of its left and right subtrees. This approach would result in an O(n^2) solution. Can you think of a more efficient way? Perhaps you could avoid repeatedly computing the heights for every node by determining balance and height in a single traversal.


# Hint 2
# We can use the Depth First Search (DFS) algorithm to compute the heights at each node. While calculating the heights of the left and right subtrees, we also check if the tree rooted at the current node is balanced. If leftHeight - rightHeight > 1, we update a global variable, such as isBalanced = False. After traversing all the nodes, the value of isBalanced indicates whether the entire tree is balanced or not.