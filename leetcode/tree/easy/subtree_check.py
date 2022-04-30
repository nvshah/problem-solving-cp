# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not (root or subRoot):  # when both root and subroot are missing
        return True

    if root and subRoot:  # when both root & subroot are present
        if root.val == subRoot.val:  # check current node values from both tree
            l = isSameTree(root.left, subRoot.left)  # check left val
            r = isSameTree(root.right, subRoot.right)  # check right val
            return l and r 

    return False


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # When root is not present at that time subroot also must not be present
    if not subRoot: return True  
    if not root: return False    

    if isSameTree(root, subRoot):  # check subtree with current level
        return True 

    if isSubtree(root.left, subRoot):  # check if subtree with left part
        return True 

    if isSubtree(root.right, subRoot): # check if subtree with right part
        return True

    return False