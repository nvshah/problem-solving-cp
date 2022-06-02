# https://leetcode.com/problems/convert-bst-to-greater-tree/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertBST(root: Optional[TreeNode]) -> Optional[TreeNode]:
    '''idea :- Reverse Inorder Traversal'''
    def greater(n, feed):
        '''
        n :- curr node {n}
        feed :- val to feed to node {n} from parent
        return sum of all nodes down this node in original BST'''
        if not n: return feed
        # 1. update right & find right sum
        rsum = greater(n.right, feed)
        # 2. update cur
        n.val += rsum
        # 3. feed & update left
        lsum = greater(n.left, n.val)  # Feed Paren Val to Left Child
        
        return lsum
            
    greater(root,0)
    return root

def convertBST2(root: Optional[TreeNode]) -> Optional[TreeNode]:
    '''idea :- Reverse Inorder Traversal'''
    curSum = 0  # track sum whilst traversing in reverse Inorder Way
    def dfs(n):
        nonlocal curSum
        # 1. Right Travel
        dfs(n.right)
        # 2. Update CurSum & node -> val
        n.val = curSum = n.val + curSum
        # 3. Left Part
        dfs(n.left)
    
    dfs(root)
    return root

