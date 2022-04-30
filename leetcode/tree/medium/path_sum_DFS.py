# https://leetcode.com/problems/path-sum/

from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    '''
     We will employ simple Depth First Search using recursion
    '''
    def dfs(node, curr_sum):
        if not node:  # no node
            return False
        
        curr_sum += node.val
        
        if not(node.left or node.right):  # Leaf Node
            return targetSum == curr_sum
        
        # explore left & right part
        return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

    return dfs(root, 0)