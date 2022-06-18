# https://leetcode.com/problems/binary-tree-cameras/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        def dfs(node):
            if not node:  # Leaf Node is Monitored & Not Camera
                return False, True
            
            c1, m1 = dfs(node.left)
            c2, m2 = dfs(node.right)
            
            camera, monitor = False, False
            
            if c1 or c2:
                monitor = True
            if not m1 or not m2:  # Need Camera to Monitor Children
                camera = True
                self.cnt += 1
                monitor = True
            
            return camera, monitor
        
        c, m = dfs(root)
        return self.cnt + (not m)  # if root is not monitored then need 1 more camera for that
                