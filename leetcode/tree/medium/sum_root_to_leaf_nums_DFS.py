# https://leetcode.com/problems/sum-root-to-leaf-numbers/


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

''' 
DFS
'''

def sumNumbers(root: Optional[TreeNode]) -> int:
    def dfs(node, currSum):
        if not node:
            return 0
        
        # add sum of curr node
        currSum = currSum * 10 + node.val 

        # if current node is leaf node then return result
        if not node.left and not node.right:
            return currSum  
        else:  # In case Not a Leaf node
            return dfs(node.left, currSum) + dfs(node.right, currSum)

    return dfs(root, 0)