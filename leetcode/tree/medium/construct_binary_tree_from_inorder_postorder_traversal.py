# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
from typing import List, Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) time | O(n) space
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {v:i for i,v in enumerate(inorder)}

        def helper(l, r):

            if l > r: return None

            root = TreeNode(postorder.pop())

            i = inorderIdx[root.val]

            # As right comes first in postorder so assigning right's root before left
            root.right = helper(i+1, r)
            root.left = helper(l, i-1)
            
            return root
            
        return helper(0, len(inorder)-1)

class Solution2:
    # O(n*logn) time
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder: return None

        rootVal = postorder.pop()

        i = inorder.index(rootVal)
        leftInorder = inorder[:i]
        rightInorder = inorder[i+1:]

        rightRoot = self.buildTree(rightInorder, postorder)
        leftRoot = self.buildTree(leftInorder, postorder)
        

        root = TreeNode(rootVal, leftRoot, rightRoot)
        return root