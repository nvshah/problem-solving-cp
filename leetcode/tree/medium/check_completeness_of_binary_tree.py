# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCompleteTree(root: Optional[TreeNode]) -> bool:
    que = deque([root])
    foundEnd = False  # encounter first null

    while que:
        n = que.popleft()
        if n:
            if foundEnd: return False  
            que.append(n.left)
            que.append(n.right)
        else:
            foundEnd = True 
    
    return True 


    