# https://leetcode.com/problems/add-one-row-to-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy = TreeNode(-1)  # dummyNode at top of tree
        dummy.left = root
        que = deque([dummy])  # queue to BFS traversal
        
        # traverse levels till depth-1
        for _ in range(depth-1):
            for _ in range(len(que)):
                node = que.popleft()
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
        
        # All the nodes at depth-1 level are present in [que] at moment
        for node in que:
            val_node = TreeNode(val)
            node.left, val_node.left = val_node, node.left  # Append to left 
            
            val_node = TreeNode(val)
            node.right, val_node.right = val_node, node.right # Append to right
        
        return dummy.left