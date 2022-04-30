# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        up = deque()
        ans = []
        up.append(root)
        
        while up:
            child = []  # child of all curr-level nodes  

            # process all current level nodes
            while up:  # Iterate current level nodes & collect their childs
                n = up.popleft()
                if n.left: child.append(n.left)
                if n.right: child.append(n.right)
            
            ans.append(n.val) # n will point to curr level last child (ie RHS child)

            up.extend(child) # add all children of current level to unProcessed Queue
        
        return ans

    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        up = deque([root])
        ans = []
        #up.append(root)
        
        while up:
            child = []  # child of all curr-level nodes  

            # process all current level nodes
            for n in up:  # Iterate current level nodes & collect their childs
                if n.left: child.append(n.left)
                if n.right: child.append(n.right)
            
            ans.append(n.val) # n will point to curr level last child (ie RHS child)

            up.extend(child) # add all children of current level to unProcessed Queue
        
        return ans