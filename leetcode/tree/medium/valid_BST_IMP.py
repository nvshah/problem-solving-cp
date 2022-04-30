# https://leetcode.com/problems/validate-binary-search-tree/submissions/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isValidBST(root: Optional[TreeNode]) -> bool:
    '''
        Idea : for each node we will check if its val is in correct bound
               So for each node we need to find the correct bound for its val
    '''
    def isValid(node, l, u):
        '''
        Check if node values is constrained between lower & upper bound recursively for children as well
        :param l: lower bound for current {node}
        :param u: upper bound for current {node}
        '''
        if not node: return True
        
        v = node.val

        if not(l < v < u):  # check current node is truely constrained
            return False
        
        left = isValid(node.left, l, v)    # check if left child is valid
        right = isValid(node.right, v, u)  # check if right child is valid
        
        return left and right  # if both left & right child follow BST principles
    
    # initially root has no connstraints for val
    return isValid(root, float('-inf'), float('inf'))