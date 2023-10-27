# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    '''BFS Traversal'''
    if not root: return []
    res = []
    que = deque([root])

    isEvenLevel = False # cur level in traversal is even or odd !

    while que:
        items = [] # items at this level
        for _ in range(len(que)):
            node = que.popleft()
            items.append(node.val)

            if node.left: que.append(node.left)
            if node.right: que.append(node.right)
        
        #level = reversed(items) if len(res)%2 else items 
        level = reversed(items) if isEvenLevel else items 
        res.append(level)
        
        isEvenLevel = not isEvenLevel
    
    return res 
            
