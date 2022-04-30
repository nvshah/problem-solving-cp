# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    '''
        preorder :- helps us to find the parent node
        inorder  :- helps us to find left & right child/sub-tree
    '''
    # There is no root node left & left-right child are reasonable only when parent is present 
    if not preorder: 
        return
    
    # 1. find the parent or root node
    val = preorder[0]
    parent = TreeNode(val)
    # find the partitioning index ie index of parent node in inorder list
    mid = inorder.index(val)
    # mid = #no elements on left part
    # 2. Find the left Child/SubTree of {parent}
    parent.left = buildTree(preorder[1: mid+1], inorder[:mid])
    parent.right = buildTree(preorder[mid+1:], inorder[mid+1:])

    return parent