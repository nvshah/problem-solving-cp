# https://leetcode.com/problems/delete-node-in-a-bst/description/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root 
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val: 
            root.right = self.deleteNode(root.right, key)
        else: 
            if not root.left: return root.right 
            if not root.right: return root.left 

            # Find Min in right sub tree
            cur = root.right 
            while cur.left:
                cur = cur.left 
                
            newVal = cur.val 
            # Delete Min in right sub tree
            root.right = self.deleteNode(root.right, newVal) 
            # Assign new val to root
            root.val = newVal
        
        return root
