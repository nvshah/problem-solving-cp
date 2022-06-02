# https://leetcode.com/problems/deepest-leaves-sum/
from typing import Optional 
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

''' DFS | map '''
def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    if not root: return 0
    m = defaultdict(int) # depth => sum
    
    def dfs(node, h):  # h -> height
        if not node: return  # surpass last level
        if not (node.left or node.right):  # reach last level
            m[h] += node.val
            return
        
        dfs(node.left, h+1)
        dfs(node.right, h+1)
        
    dfs(root, 0)
    
    depth = max(m)  # deepest level
    return m[depth]