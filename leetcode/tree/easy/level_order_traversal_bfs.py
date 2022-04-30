# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    q = deque([root])
    ans = []
    while q:
        l = []
        # process q 
        for i in range(len(q)):  # current level nodes traversal
            n = q.popleft()  # extract left most element
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
            l.append(n.val)
        ans.append(l)  # curr level elements
    return ans

