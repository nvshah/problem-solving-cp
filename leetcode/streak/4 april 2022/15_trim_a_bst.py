# https://leetcode.com/problems/trim-a-binary-search-tree
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(n):
            if not n: return 
            v = n.val
            if v < low:
                # as all left part will be ineligible (BST property)
                return trim(n.right)            
            elif v > high:
                # all right part ineligible (BST property)
                return trim(n.left)
            else:
                # current node satisfies [low, high] so check for children
                n.left = trim(n.left)
                n.right = trim(n.right)
            return n
        return trim(root)
                
                
                
                