# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Idea
As BST inline traversal gives sorted array
& min-distance in sorted array can be found between adjacent position only
'''

# O(n) time | O(n) space
def minDiffInBST(root: Optional[TreeNode]) -> int:
    '''Inline Traversal'''

    prev = TreeNode(float('-inf')) # pointer to previous position, whilst inline traversal
    minDiff = float('inf')

    def dfs(node):
        '''inline traversal'''
        if not node: return 
        nonlocal prev, minDiff

        dfs(node.left)

        # Process
        minDiff = min(minDiff, node.val-prev.val) # [prev] is previous to [node] in inline traversal
        prev = node  # [node] becomes previous for [node.right]

        dfs(node.right) 
    
    dfs(root)
    return minDiff