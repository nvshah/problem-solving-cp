
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root: return root
#         cur = root  # current layer
#         nxt = cur.left if cur.left else cur.right # next layer (ie below layer in depth)
#         end = nxt

#         while nxt: # do BFS (layer by layer) where current layer :- {cur}
            

#             if cur.left:
#                 if cur.right:
#                     cur.left.next = cur.right # link the children ie left -> right
#                     end = cur.right
#                 else:
#                     end = cur.left
#             else:
#                 if not cur.right:
#                     cur = cur.next

#             if cur.next: 
#                 # link between children of 2 sibblings
#                 lnk = cur.next.left if cur.next.left else cur.next.right
#                 end.next = lnk

#                 # go to next sibbling at current level
#                 cur = cur.next 
#             else:
#                 # as current level traversal completes, All children nodes of {cur} level are linked
#                 cur = nxt # go to next level
#                 nxt = nxt.left if nxt.left else nxt.right # record new upcoming layer after updated {cur}
        
#         return root

def connect(root: 'Node') -> 'Node':
    if not root: return root
    q = deque([root])  # Queue for BFS
    
    while q:
        dummy = Node(-1)  # dummy (ie head ) for curr level linking
        for i in range(len(q)):
            n = q.popleft()
            dummy.next, dummy = n, n
            
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
    
    return root