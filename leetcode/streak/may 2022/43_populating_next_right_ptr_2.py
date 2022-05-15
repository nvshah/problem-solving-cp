
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect1(root: 'Node') -> 'Node':
    ''' O(n) T.C :- (BFS + Queue) '''
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

def connect2(root: 'Node') -> 'Node':
    '''O(1) space complexity via Pointers to next level
       BFS + Pointers
    '''
    if not root: return root

    # current layer first node
    cur = root
    end = Node(-1)   # dummy node for cur level
    t = cur  # temp ptr to first node of cur-level

    while True:
        # Link the Below Layer (of cur)
        if cur.left:
            end.next = end = cur.left
            
        if cur.right:
            end.next = end = cur.right

        if cur.next:  # same layer
            cur = cur.next 
        else:
            end = Node(-1) # next layer new dummy node
            
            # Find next layer first
            nxt = None 
            while t and nxt == None:
                nxt = t.left if t.left else t.right
                t = t.next

            if not nxt: break  # no next level
            t = cur = nxt  # next level becomes now current