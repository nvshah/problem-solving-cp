# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
    def dfs(node):
        ''' Return :- height, status of balanced tree or not '''
        if not node:
            return 0, True
        left, status_l = dfs(node.left)
        right, status_r = dfs(node.right)

        if not(status_l and status_r) or abs(left - right) > 1:
            return -1, False 
        
        return 1 + max(left, right), True
    return dfs(root)[1]