# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal1(root: Optional[TreeNode]) -> List[int]:
    '''Recursively'''
    res = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
    #initiate the traversal
    inorder(root)
    return res

def inorderTraversal2(root: Optional[TreeNode]) -> List[int]:
    '''Stack + Iterative Manner'''
    res = []
    curr = root  # pointer to current node
    stack = []   # stack to keep track of node at upper levels

    while curr or stack:  # till any node exists
        # 1. Explore the Depth First Left Most
        while curr:
            stack.append(curr)
            curr = curr.left
        # 2. Add the Top-most elem on stack to {res}
        top = stack.pop()
        res.append(top.val)
        # 3. Explore the Right Part for {top}
        curr = top.right

    return res
