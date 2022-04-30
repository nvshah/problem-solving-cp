# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
from typing import Optional

"""

"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        cur = root  # current layer
        nxt = root.left # next layer (ie below layer in depth)

        while nxt: # do BFS (layer by layer) where current layer :- {cur}
            cur.left.next = cur.right # link the children ie left -> right
            if cur.next: 
                # link between children of 2 sibblings
                cur.right.next = cur.next.left 

                # go to next sibbling at current level
                cur = cur.next 
            else:
                # as current level traversal completes, All children nodes of {cur} level are linked
                cur = nxt # go to next level 
                nxt = nxt.left # record new upcoming layer after updated {cur}
        
        return root
        




        