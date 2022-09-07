# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

''' Post Order Traversal Approach '''
def pruneTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def trav(n):
        ''' return True if all nodes are 0 in a tree formed by root node [n] '''
        if not n: return True
        
        isLeftAllZero = trav(n.left)
        isRightAllZero = trav(n.right)
        
        if isLeftAllZero: n.left = None
        if isRightAllZero: n.right = None
        
        return isLeftAllZero and isRightAllZero and n.val==0 
            
    allZero = trav(root)
    return root if not allZero else None
        