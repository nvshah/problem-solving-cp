# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
from collections import deque


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    '''DFS (Pre-Order Traversal) '''
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def isSameTree2(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    '''BFS (Level-Order Traversal) '''
    pQue = deque([p])
    qQue = deque([q])

    while (pQue and qQue):
        # to keep track of child nodes of curr level nodes
        pList = []
        qList = []
        while pQue and qQue:
            # (PICK)
            nodeP = pQue.popleft()
            nodeQ = qQue.popleft()
            
            if not nodeQ and not nodeP: continue
            if not nodeP or not nodeQ: return False

            if nodeP.val != nodeQ.val:
                return False 

            # (PROCESS) Add respective child elements at below level for corresp Tree
            pList.extend([nodeP.left, nodeP.right])
            qList.extend([nodeQ.left, nodeQ.right])
        else:
            # un-Equal Nodes between Trees
            if pQue or qQue: return False

        # Add all respective child elements at below level for curr Tree
        pQue.extend(pList)
        qQue.extend(qList)
    else:
        # un-Equal Nodes between Trees
        if pQue or qQue: return False
        return True