# https://leetcode.com/problems/search-in-a-binary-search-tree/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST1(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    '''Iterative'''
    while True:
        # if not root:
        #     return None
        if not root or val == root.val:
            return root
        if val < root.val:
            root = root.left
        else:
            root = root.right

def searchBST2(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    '''Recursive'''
    # if not root: return root 
    if not root or val == root.val: return root
    if val < root.val:
        return searchBST2(root.left, val)
    return searchBST2(root.right, val)

