
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = [] 

        def helper(node):
            if not node:
                return 
            # process all children (from l -> r)
            for n in node.children:
                helper(n)
            # process self
            res.append(node.val)

        helper(root) 
        return res

    def postorder_iter(self, root: 'Node') -> List[int]:
        res = [] 
        stack = [(root, False)] # (node, isProcessed)

        while stack: 
            node, isProcessed = stack.pop()

            if isProcessed:
                res.append(node.val)
                continue 

            if not node: 
                continue 

            # Node is now prcocessed (as all children will be accounted)
            stack.append((node, True))
            
            # As we want leftmost on top of stack so used `reversed()`
            for n in reversed(node.children):
                stack.append((n, False)) 
        
        return res
            

