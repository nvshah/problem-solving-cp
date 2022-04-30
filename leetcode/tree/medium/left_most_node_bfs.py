# https://leetcode.com/problems/find-bottom-left-tree-value/

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findBottomLeftValue(root: Optional[TreeNode]) -> int:
    '''
    idea : use BFS ie Level Order Traversal (Iteration + queue)
    '''

    #! AIm : At each level we will traverse from Right -> left as we intend to find the leftmost at last
    unprocessed = deque()  # queue that will hold the unprocessed nodes of tree
    last_processed = None  # last processed node exited from unproessed queue

    unprocessed.append(root)
    while unprocessed:
        # 1. remove the node in Queue from left side
        n = unprocessed.popleft()
        #l, r = n.left, n.right
        *sibblings, = n.right, n.left  # right to left

        # 2. add the children of nodes to Queue
        for s in sibblings:
            if s:
                unprocessed.append(s)
        
        last_processed = n.val # update last processed value

    return last_processed



