# https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/
from typing import Optional, List



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        trav = []
        
        def pre(node):
            if not node: return
            trav.append(node.val)
            pre(node.left)
            pre(node.right)
        
        pre(root)
        return trav
        
            
        