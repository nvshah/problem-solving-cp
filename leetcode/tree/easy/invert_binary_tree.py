# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def helper(n):
        if not n:
            return

        l, r = n.left, n.right  # left & right childof current node n

        helper(l)  # invert left part 
        helper(r)  # invert right part

        n.left, n.right = r, l # swap left & right part
    
    helper(root)
    return root