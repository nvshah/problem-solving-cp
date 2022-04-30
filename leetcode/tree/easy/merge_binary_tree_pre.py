# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 and not root2: # reach to ground level of both the tree
        return None 
    
    # left & right nodes tracking for current node in both the trees
    n1l = n1r = n2l = n2r = None
    v1 = v2 = 0   # values of currennt parent node in both the trees

    if root1:
        v1 = root1.val
        n1l, n1r  = root1.left, root1.right  # left & right child of root1
    
    if root2:
        v2 = root2.val
        n2l, n2r  = root2.left, root2.right # left & right child of root2

    node = TreeNode(v1 + v2)
    node.left = mergeTrees(n1l, n2l)
    node.right = mergeTrees(n1r, n2r)

    return node

