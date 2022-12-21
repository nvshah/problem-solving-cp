# https://leetcode.com/problems/leaf-similar-trees/
from typing import Optional

# Ref https://leetcode.com/ju40268/
#     https://leetcode.com/problems/leaf-similar-trees/solutions/152319/python-recursion/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        :param root1: TreeNode
        :param root2: TreeNode
        :rtype: bool

        Concept :_ DFS, Generator
        """
        def leaf(root):
            if not (root.left or root.right):
                yield root.val # reach the leaf
            
            # Explore Left
            if root.left:
                for key in leaf(root.left):
                    yield key
            
            # Explore Right
            if root.right:
                for key in leaf(root.right):
                    yield key


        return list(leaf(root1)) == list(leaf(root2))