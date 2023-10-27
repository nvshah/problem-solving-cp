# https://leetcode.com/problems/symmetric-tree
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(slef, root: Optional[TreeNode]) -> bool:
        
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False 
            
            return (left.val == right.val 
                and dfs(left.left, right.right)   # Outer
                and dfs(left.right, right.left))  # Inner
        
        return dfs(root.left, root.right) if root else True