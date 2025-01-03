from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if not root:
                return None
            root.left = invert(root.left)
            root.right = invert(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            return root
        return invert(root)

#2. Depth First Search
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root


# Invert Binary Tree
# You are given the root of a binary tree root. Invert the binary tree and return its root.

# Example 1:



# Input: root = [1,2,3,4,5,6,7]

# Output: [1,3,2,7,6,5,4]
# Example 2:



# Input: root = [3,2,1]

# Output: [3,1,2]
# Example 3:

# Input: root = []

# Output: []
# Constraints:

# 0 <= The number of nodes in the tree <= 100.
# -100 <= Node.val <= 100


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the tree.


# Hint 1
# From the diagram, you can see that the left and right children of every node in the tree are swapped. Can you think of a way to achieve this recursively? Maybe an algorithm that is helpful to traverse the tree.


# Hint 2
# We can use the Depth First Search (DFS) algorithm. At each node, we swap its left and right children by swapping their pointers. This inverts the current node, but every node in the tree also needs to be inverted. To achieve this, we recursively visit the left and right children and perform the same operation. If the current node is null, we simply return.